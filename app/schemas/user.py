from typing import Optional, List

from pydantic import BaseModel, EmailStr

from .user_service import UserService


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr]
    is_active: Optional[bool] = True
    is_superuser: bool
    full_name: Optional[str]
    is_technician: bool
    is_customer: bool
    color: Optional[str]


# Properties to receive via API on creation
class UserCreate(UserBase):
    document_id: int
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    services: Optional[List[UserService]]


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
