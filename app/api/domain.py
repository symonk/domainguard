from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.glue import new_db_session
from sqlalchemy.ext.asyncio import AsyncSession
import json

router = APIRouter()


class Pretty(JSONResponse):
    def render(self, content: any) -> bytes:
        return json.dumps(content, ensure_ascii=False, indent=4).encode("utf-8")

@router.get("/check", response_class=Pretty)
async def check(db: AsyncSession = Depends(new_db_session)):
    return {"foo": "bar"}
