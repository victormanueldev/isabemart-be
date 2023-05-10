from typing import Optional, List
from pydantic import BaseModel


class HeadquarterBase(BaseModel):
    name: str
    city: str
    neighborhood: str
    address: str
    phone: str


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
    pass
