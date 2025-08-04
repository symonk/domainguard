from fastapi import APIRouter, Depends
from app.glue import new_db_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("/check")
async def check(db: AsyncSession = Depends(new_db_session)):
    return {
        "foo": "bar"
    }
