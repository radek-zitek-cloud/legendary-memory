"""API routers for the auth service."""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud, schemas
from .database import get_session
from .security import create_access_token, get_password_hash, verify_password

router = APIRouter()


@router.post("/register", response_model=schemas.UserRead, status_code=status.HTTP_201_CREATED)
async def register_user(user_in: schemas.UserCreate, session: AsyncSession = Depends(get_session)):
    """Register a new user."""
    existing = await crud.get_user_by_username(session, user_in.username)
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    user = await crud.create_user(session, user_in.username, get_password_hash(user_in.password))
    return user


@router.post("/login", response_model=schemas.Token)
async def login(user_in: schemas.UserCreate, session: AsyncSession = Depends(get_session)):
    """Authenticate a user and return a JWT token."""
    user = await crud.get_user_by_username(session, user_in.username)
    if not user or not verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token({"sub": str(user.id)})
    return schemas.Token(access_token=token)
