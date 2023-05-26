from typing import Optional, Any

from pydantic import BaseModel


class AreaBase(BaseModel):
    customer_id: Optional[int]
    headquarter_id: Optional[int]
    name: Optional[str]
    estimated_time: Optional[str]
    incidence: Optional[bool]
    activity_level: Optional[str]


class AreaCreate(AreaBase):
    pass


class AreaUpdate(AreaBase):
    pass


class AreaInDBBase(AreaBase):
    id: int

    class Config:
        orm_mode = True


class Area(AreaInDBBase):
    customer: Optional[Any] = None
    headquarter: Optional[Any] = None
    pass
