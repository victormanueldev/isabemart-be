from typing import Optional, List
from pydantic import BaseModel, EmailStr

from .headquarter import HeadquarterCreate, Headquarter


class CustomerBase(BaseModel):
    document_id: str
    customer_type: str
    commercial_name: Optional[str] = None
    email: EmailStr
    city: str
    address: str
    phone: str


class CustomerCreate(CustomerBase):
    headquarter: Optional[HeadquarterCreate] = None
    pass


class CustomerUpdate(CustomerBase):
    id: int
    pass


class CustomerInDBBase(CustomerBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class Customer(CustomerInDBBase):
    headquarters: Optional[List[Headquarter]] = None
    pass
