from fastapi import FastAPI

from app.api import domain

app = FastAPI(title="Domain Guard")
app.include_router(domain.router, prefix="/domains", tags=("domains",))
