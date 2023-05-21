from typing import Optional

from pydantic import BaseModel


class SanityPlanBase(BaseModel):
    visits_qty: Optional[int]
    frequency: Optional[str]
    customer_id: Optional[int]


class SanityPlanCreate(SanityPlanBase):
    pass


class SanityPlanUpdate(SanityPlanBase):
    pass


class SanityPlanInDBBase(SanityPlanBase):
    id: int

    class Config:
        orm_mode = True


class SanityPlan(SanityPlanInDBBase):
    pass
