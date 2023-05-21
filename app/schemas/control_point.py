from typing import Optional

from pydantic import BaseModel


class ControlPointBase(BaseModel):
    name: Optional[str]
    status: Optional[str]
    observations: Optional[str]
    area_id: Optional[int]
    customer_id: Optional[int]
    headquarter_id: Optional[int]


class ControlPointCreate(ControlPointBase):
    pass


class ControlPointUpdate(ControlPointBase):
    pass


class ControlPointInDBBase(ControlPointBase):
    id: Optional[int]

    class Config:
        orm_mode = True


class ControlPoint(ControlPointInDBBase):
    pass
