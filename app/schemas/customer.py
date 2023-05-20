from typing import Optional, List, Any

from pydantic import BaseModel, EmailStr

from .headquarter import HeadquarterCreate


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
    pass


class CustomerInDBBase(CustomerBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class Customer(CustomerInDBBase):
    services: Optional[List[Any]]
    pass
