from fastapi import APIRouter, Depends
from app.glue import new_db_session
from app.services import WhoisService
from app.glue import new_whois_service
from sqlalchemy.ext.asyncio import AsyncSession

v1_domain_router = APIRouter(prefix="/api/v1")


@v1_domain_router.get("/analyse/{domain}")
def check(domain: str, whois_service: WhoisService = Depends(new_whois_service), db: AsyncSession = Depends(new_db_session)):
    response = whois_service.whois(domain)
    return response
