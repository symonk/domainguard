from fastapi import FastAPI

from app.api import domain
from app.api import health

app = FastAPI(title="Domain Guard")
app.include_router(domain.v1_domain_router, prefix="/domains", tags=("domains",))
app.include_router(health.healthRouter, tags=("health",))
