import datetime
import decimal
import json

import uvicorn
from fastapi import Request, status, HTTPException, Response, Depends
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from passlib.handlers.sha2_crypt import sha512_crypt as crypto
from typing import Dict, List, Union

from General import config as cfg
from General.database import DictRecord
from General.modules.forms import RegForm, LoginForm
from General.oauth2 import authenticate_user, create_access_token, get_current_user_from_cookie, decode_token

from loader import app, db

#  https://samedwardes.com/2022/04/14/fastapi-webapp-with-auth/


def json_encoder(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    elif isinstance(obj, DictRecord):
        return obj.to_dict()
    elif isinstance(obj, decimal.Decimal):
        return int(obj)

    raise TypeError(f"{obj} is not JSON serializable")


@app.post("/auth/check_auth")
async def check_auth(request: Request):
    decoded = await get_current_user_from_cookie(request)
    if decoded["ok"]:
        decoded["user"] = decoded["user"].to_dict()
    return JSONResponse(content=decoded)


@app.post("token")
async def login_for_access_token(
        response: Response,
        form_data: OAuth2PasswordRequestForm = Depends()) -> Dict[str, str]:
    user = await authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")

    access_token = create_access_token(data={"username": user["username"]})

    response.set_cookie(key=cfg.COOKIE_NAME, value=f"Bearer {access_token}", httponly=True)
    return {cfg.COOKIE_NAME: access_token, "token_type": "bearer"}


def check_params(transmitted_params: dict, needed_params: List[list]) -> Union[None, dict]:
    error = None

    for par in needed_params:
        if par[0] not in transmitted_params.keys():
            error = dict(ok=False, err=f"Параметр \"{par[0]}\" отсутсвует!")
        else:
            if not isinstance(transmitted_params[par[0]], par[1]):
                error = dict(
                    ok=False,
                    err=f"Неверный тип у метода \"{transmitted_params[par[0]]}\". "
                        f"Передан - {type(transmitted_params[par[0]])}, требуется - {par[1]}"
                )

    return error


@app.post("/api")
async def api(request: Request) -> Dict[str, str]:
    data = await request.json()
    user = await decode_token(request.cookies.get(cfg.COOKIE_NAME))

    methods_no_auth = ["get_posts", "get_last_posts"]

    if "method" not in data:
        return JSONResponse(dict(ok=False, err="Параметр \"method\" остутствует!"))

    method = str(data["method"])

    if method not in methods_no_auth:
        if not user["ok"]:
            return JSONResponse(user)

    match method:
        case "get_posts":
            checked = check_params(data, [["username", str]])
            if checked is not None:
                return JSONResponse(checked)

            response = await db.get_user_posts(data["username"])
            return JSONResponse(dict(ok=True, posts=response))

        case "get_last_posts":
            response = await db.get_last_posts()
            return JSONResponse(dict(ok=True, posts=response))

        case "get_my_posts":
            checked = check_params(data, [["username", str]])
            if checked is not None:
                return JSONResponse(checked)

            response = await db.get_user_posts(data["username"])
            return JSONResponse(dict(ok=True, posts=response))

        case "create_post":
            checked = check_params(data, [["title", str], ["description", str], ["tags", list]])
            if checked is not None:
                return JSONResponse(checked)

            await db.create_post(username=user["user"]["username"], title=data["title"], description=data["description"], tags=data["tags"])
            return JSONResponse(dict(ok=True))

    return JSONResponse(dict(ok=True))


@app.post("/auth/registration", response_class=HTMLResponse)
async def login_post(request: Request):
    form = RegForm(request)
    await form.load_data()

    if await form.is_valid():
        response = await db.create_user(form.email, form.username, crypto.hash(form.password))

        if response:
            response = RedirectResponse("/", status.HTTP_302_FOUND)
            await login_for_access_token(response=response, form_data=form)
            return response

        form.errors.append("The user already exists")

    return JSONResponse(content=dict(ok=False, errors=form.errors))


@app.post("/auth/login", response_class=HTMLResponse)
async def login_post(request: Request):
    form = LoginForm(request)
    await form.load_data()

    if await form.is_valid():
        try:
            response = RedirectResponse("/", status.HTTP_302_FOUND)
            await login_for_access_token(response=response, form_data=form)
            return response
        except HTTPException:
            form.errors.append("Incorrect Username or Password")

    return JSONResponse(content=dict(ok=False, errors=form.errors))


@app.post("/auth/logout", response_class=HTMLResponse)
def login_get():
    response = RedirectResponse("/", status.HTTP_302_FOUND)
    response.delete_cookie(cfg.COOKIE_NAME)
    return response


if __name__ == "__main__":
    uvicorn.run(app, host=cfg.host, port=cfg.port)

