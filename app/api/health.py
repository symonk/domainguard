import time
from fastapi import APIRouter

now = time.monotonic()

healthRouter = APIRouter()


@healthRouter.get("/health")
def handle():
    return {"uptime": f"{int(time.monotonic() - now)} seconds"}


