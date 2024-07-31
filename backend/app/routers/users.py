from datetime import timedelta

from app.settings import ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.enum import UserType
from app.model import User
from app.schemas.user import Token, UserCreate, UserRead
from app.utils.auth import (authenticate_user, create_access_token,
                            get_password_hash)

router = APIRouter()

@router.post("/token", response_model=Token)
async def create_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)

    return Token (
        access_token=access_token,
        token_type="Bearer",
        user_type=user.user_type,
    )


@router.post("/create", response_model=UserRead, include_in_schema=True,)
def create_admin(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    user_query = db.query(User).filter(User.username == user.username).first()
    if user_query:
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_password = get_password_hash(user.password)
    add_user = User(
        username=user.username,
        password=hashed_password,
        user_type=UserType.ADMIN.value,
    )
    db.add(add_user)
    db.commit()
    db.refresh(add_user)
    return add_user