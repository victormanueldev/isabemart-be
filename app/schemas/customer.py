from typing import Optional, List, Any

from pydantic import BaseModel, EmailStr

from .headquarter import HeadquarterCreate


class CustomerBase(BaseModel):
    document_id: Optional[str]
    customer_type: Optional[str]
    commercial_name: Optional[str] = None
    email: Optional[EmailStr]
    city: Optional[str]
    address: Optional[str]
    phone: Optional[str]


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
    control_points: Optional[List[Any]]
    sanity_plans: Optional[List[Any]]
    documents: Optional[List[Any]]
    pass
