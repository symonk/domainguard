import typing

from app.db import SessionLocal
from app.services.whois import WhoisService
from sqlalchemy.ext.asyncio import AsyncSession


async def new_db_session() -> typing.AsyncGenerator[AsyncSession, None]:
    """get_db yields a new async database session"""
    async with SessionLocal() as session:
        yield session


def new_whois_service() -> WhoisService:
    """new_whois_service instantiates and returns a new whois service."""
    return WhoisService()