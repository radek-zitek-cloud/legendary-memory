"""Pydantic schemas for the auth service."""
from __future__ import annotations

from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    """Data required to register a new user."""

    username: str = Field(..., max_length=50)
    password: str = Field(..., min_length=4)


class UserRead(BaseModel):
    """Representation of a user returned via API."""

    id: int
    username: str

    class Config:
        from_attributes = True


class Token(BaseModel):
    """JWT access token."""

    access_token: str
    token_type: str = "bearer"
