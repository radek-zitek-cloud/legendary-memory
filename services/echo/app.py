"""FastAPI application for the echo service."""
from __future__ import annotations

from fastapi import FastAPI

from .routers import router

app = FastAPI(title="Echo Service", version="0.1.0")

app.include_router(router)
