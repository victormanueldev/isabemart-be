from typing import Optional, Any, List
from datetime import datetime, time
from pydantic import BaseModel

from .user import UserService
from .treatment import TreatmentService


class ServiceBase(BaseModel):
    customer_id: Optional[int]
    headquarter_id: Optional[int]
    invoice_id: Optional[int]
    service_type: Optional[str]
    expected_date: Optional[datetime]
    executed_date: Optional[datetime]
    start_time: Optional[time]
    end_time: Optional[time]
    observations: Optional[str]


class ServiceCreate(ServiceBase):
    user_id: int
    treatments: List[int] = []
    pass


class ServiceUpdate(ServiceBase):
    pass


class ServiceInDBBase(ServiceBase):
    id: int

    class Config:
        orm_mode = True


class Service(ServiceInDBBase):
    users: Optional[List[UserService]]
    treatments: Optional[List[TreatmentService]]
    pass
