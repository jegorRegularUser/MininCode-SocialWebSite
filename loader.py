from contextlib import asynccontextmanager

from fastapi import FastAPI

from General.database import DB
from General.modules.oauth2_password_bearer_with_cookie import OAuth2PasswordBearerWithCookie


@asynccontextmanager
async def lifespan(_):
    await db.init_database()
    yield


app = FastAPI(lifespan=lifespan)
oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="token")

db: DB = DB()


