from typing import Optional
from pydantic import BaseModel


class TreatmentBase(BaseModel):
    name: Optional[str]
    cost: Optional[int]
    frequency: Optional[str]


class TreatmentCreate(TreatmentBase):
    pass


class TreatmentUpdate(TreatmentBase):
    pass


class TreatmentInDBBase(TreatmentBase):
    id: Optional[int]

    class Config:
        orm_mode = True


class Treatment(TreatmentInDBBase):
    pass


class TreatmentService(BaseModel):
    treatment: Treatment
