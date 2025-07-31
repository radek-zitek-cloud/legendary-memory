"""Tests for the echo service."""
from __future__ import annotations

from fastapi.testclient import TestClient

from services.echo.app import app

client = TestClient(app)


def test_echo() -> None:
    """Echo endpoint should return provided message."""
    response = client.get("/echo", params={"message": "hello"})
    assert response.status_code == 200
    assert response.json() == {"message": "hello"}
