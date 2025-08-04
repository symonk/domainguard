from fastapi import APIRouter, Depends
from glue import new_db_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("/check")
async def check(db: AsyncSession = Depends(new_db_session)):
    return
