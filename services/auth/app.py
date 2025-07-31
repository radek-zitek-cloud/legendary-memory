"""FastAPI application for the auth service."""
from __future__ import annotations

from fastapi import FastAPI

from . import models
from .database import engine
from .routers import router

app = FastAPI(title="Auth Service", version="0.1.0")


@app.on_event("startup")
async def on_startup() -> None:
    """Create database tables on startup."""
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


app.include_router(router, prefix="/auth")
