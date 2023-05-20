from typing import Optional

from pydantic import BaseModel

from .customer import Customer
from .headquarter import Headquarter


class AreaBase(BaseModel):
    customer_id: Optional[int]
    headquarter_id: Optional[int]
    name: Optional[str]
    estimated_time: Optional[str]


class AreaCreate(AreaBase):
    pass


class AreaUpdate(AreaBase):
    pass


class AreaInDBBase(AreaBase):
    id: int

    class Config:
        orm_mode = True


class Area(AreaInDBBase):
    customer: Optional[Customer] = None
    headquarter: Optional[Headquarter] = None
    pass
