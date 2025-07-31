"""Data access utilities for the auth service."""
from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import User


async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
    """Retrieve a user by username."""
    result = await session.execute(select(User).where(User.username == username))
    return result.scalars().first()


async def create_user(session: AsyncSession, username: str, hashed_password: str) -> User:
    """Create and persist a new user."""
    user = User(username=username, hashed_password=hashed_password)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
