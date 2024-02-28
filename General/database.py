import datetime

import asyncpg
from loguru import logger
from typing import List, Union, Any

from General import config as cfg


class DictRecord(asyncpg.Record):
    def __getitem__(self, key) -> Any:
        value = super().__getitem__(key)
        if isinstance(value, asyncpg.Record):
            return DictRecord(value)

        return value

    def to_dict(self) -> dict:
        return self._convert_records_to_dicts(dict(super().items()))

    def _convert_records_to_dicts(self, obj) -> dict:
        if isinstance(obj, dict):
            return {k: self._convert_records_to_dicts(v) for k, v in obj.items()}
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, list):
            return [self._convert_records_to_dicts(item) for item in obj]
        elif isinstance(obj, asyncpg.Record):
            return dict(obj)
        else:
            return obj

    def __repr__(self) -> str:
        return str(self.to_dict())


class DB:
    db: asyncpg.Pool

    async def close(self) -> None:
        await self.db.close()

    async def init_database(self) -> None:
        self.db = await asyncpg.create_pool(
            host=cfg.db_host,
            port=cfg.db_port,
            user=cfg.db_username,
            password=cfg.db_password,
            database=cfg.db_name,
            record_class=DictRecord
        )

        await self._crete_tables()
        logger.success("База данных инициализирована успешно!")

    async def _crete_tables(self) -> None:
        await self.db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                email TEXT NOT NULL,
                username TEXT NOT NULL PRIMARY KEY,
                hashed_password TEXT NOT NULL
            );
        """)
        await self.db.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id SERIAL PRIMARY KEY NOT NULL,
                username TEXT NOT NULL,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                tags TEXT[],
                date_of_creation TIMESTAMP DEFAULT now()
            );
        """)

    async def create_user(self, email: str, username: str, hashed_password: str) -> bool:
        try:
            await self.db.execute(
                "INSERT INTO users(email, username, hashed_password) VALUES($1, $2, $3)",
                email, username, hashed_password
            )

            return True
        except asyncpg.exceptions.UniqueViolationError:
            return False

        except Exception:
            return False

    async def get_user(self, username: str) -> Union[DictRecord, None]:
        response = await self.db.fetchrow("SELECT * FROM users WHERE username=$1", username)
        return response

    async def get_user_posts(self, username: str) -> List[dict]:
        response = await self.db.fetch("SELECT * FROM posts WHERE username=$1", username)
        return [i.to_dict() for i in response]

    async def get_last_posts(self):
        response = await self.db.fetch("""
            SELECT * FROM posts
            ORDER BY date_of_creation DESC
            LIMIT 10;
        """)
        return [i.to_dict() for i in response]

    async def create_post(self, username: str, title: str, description: str, tags: Union[None, List[str]]) -> None:
        await self.db.execute(
            "INSERT INTO posts (title, description, tags, username) VALUES ($1, $2, $3, $4)",
            title, description, tags, username
        )

    async def update_post(
            self, id: int, title: Union[None, str],
            description: Union[str, None], tags: Union[None, List[str]]) -> None:
        await self.db.execute(
            f"UPDATE posts SET title = $1, description = $2, tags = $3 WHERE id=$4",
            title, description, tags, id
        )

    async def delete_post(self, id: int) -> None:
        await self.db.execute(f"DELETE FROM posts WHERE id=$1", id)
