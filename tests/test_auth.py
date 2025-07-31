"""Tests for the auth service."""
from __future__ import annotations

from fastapi.testclient import TestClient

from services.auth.app import app
from services.auth.models import Base
from services.auth.database import engine

client = TestClient(app)


def test_register_and_login(tmp_path) -> None:
    """Register a user and then log in."""
    # Ensure tables exist for the test database
    import asyncio

    async def create_tables() -> None:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    asyncio.run(create_tables())
    response = client.post("/auth/register", json={"username": "alice", "password": "secret"})
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "alice"

    response = client.post("/auth/login", json={"username": "alice", "password": "secret"})
    assert response.status_code == 200
    token = response.json().get("access_token")
    assert token
