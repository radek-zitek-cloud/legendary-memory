"""Routers for the echo service."""
from __future__ import annotations

from fastapi import APIRouter

router = APIRouter()


@router.get("/echo")
async def echo(message: str) -> dict[str, str]:
    """Return the received message."""
    return {"message": message}
