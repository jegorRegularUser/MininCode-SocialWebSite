import datetime
import datetime as dt
from jose import jwt, JWTError, ExpiredSignatureError
from typing import Dict, Union
from fastapi import HTTPException, status, Request, Depends

from passlib.handlers.sha2_crypt import sha512_crypt as crypto

from General import config as cfg
from General.database import DictRecord
from loader import db, oauth2_scheme


def create_access_token(data: Dict) -> str:
    to_encode = data.copy()
    expire = dt.datetime.utcnow() + dt.timedelta(minutes=cfg.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        cfg.SECRET_KEY,
        algorithm=cfg.ALGORITHM
    )
    return encoded_jwt


async def authenticate_user(username: str, plain_password: str) -> Union[bool, DictRecord]:
    user = await db.get_user(username)

    if user is None:
        return False

    if not crypto.verify(plain_password, user["hashed_password"]):
        return False

    return user


async def decode_token(token: str) -> DictRecord:
    if token is None:
        return dict(ok=False, err="Could not validate credentials")

    token = token.removeprefix("Bearer").strip()

    try:
        payload = jwt.decode(token, cfg.SECRET_KEY, algorithms=[cfg.ALGORITHM])
        username: str = payload.get("username")

        if username is None:
            return dict(ok=False, err="Could not validate credentials")

    except ExpiredSignatureError:
        return dict(ok=False, err="Signature has expired")

    user = await db.get_user(username)
    return dict(ok=True, user=user)


async def get_current_user_from_cookie(request: Request) -> DictRecord:
    token = request.cookies.get(cfg.COOKIE_NAME)
    decoded = await decode_token(token)
    return decoded
