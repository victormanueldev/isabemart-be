from typing import Optional, List
from pydantic import BaseModel

from .customer import Customer
from .headquarter import Headquarter


class AreaBase(BaseModel):
    name: str
    estimated_time: str


class AreaCreate(AreaBase):
    pass


class AreaInDBBase(AreaBase):
    id: int
    customer_id: int
    headquarter_id: int

    class Config:
        orm_mode = True


class Area(AreaInDBBase):
    pass
