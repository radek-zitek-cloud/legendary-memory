"""Database configuration for the auth service."""
from __future__ import annotations

import os
from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

DATABASE_URL = os.environ.get(
    "DATABASE_URL", "sqlite+aiosqlite:///./auth.db"
)

engine = create_async_engine(DATABASE_URL, echo=False)

AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_session() -> AsyncIterator[AsyncSession]:
    """Dependency that provides an async database session."""
    async with AsyncSessionLocal() as session:
        yield session
