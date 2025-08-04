import typing

from app.db import SessionLocal
from sqlalchemy.ext.asyncio import AsyncSession


async def new_db_session() -> typing.AsyncGenerator[AsyncSession, None]:
    """get_db yields a new async database session"""
    async with SessionLocal() as session:
        yield session
