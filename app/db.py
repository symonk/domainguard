from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from app.config import settings

from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_async_engine(settings.db_url, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()
