from typing import Optional

from app.enum import UserType
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str
    user_type: UserType


class TokenData(BaseModel):
    username: str


class UserBase(BaseModel):
    username: str
    email: Optional[str] = None


class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    user_type: UserType

    class Config:
        orm_mode = True