

from pydantic import BaseModel, EmailStr
from typing import Optional, List
import datetime
import uuid


class UserCreate(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    password: str


class UserOut(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    created_at: datetime.datetime

    class Config:
        orm_mode = True



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str



class SessionBase(BaseModel):
    user_id: int


class SessionCreate(SessionBase):
    pass


class Session(SessionBase):
    session_id: uuid.UUID
    start_time: datetime.datetime
    end_time: Optional[datetime.datetime]
    overall_score: Optional[int]

    class Config:
        orm_mode = True
