from typing import Optional, Any
from pydantic import BaseModel


class HeadquarterBase(BaseModel):
    name: Optional[str]
    city: Optional[str]
    neighborhood: Optional[str]
    address: Optional[str]
    phone: Optional[str]


class HeadquarterCreate(HeadquarterBase):
    pass


class HeadquarterUpdate(HeadquarterBase):
    pass


class HeadquarterInDBBase(HeadquarterBase):
    id: int
    customer_id = int

    class Config:
        orm_mode = True


class Headquarter(HeadquarterInDBBase):
    customer: Optional[Any] = None
    pass
