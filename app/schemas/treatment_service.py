from datetime import datetime, time
from typing import Any, Optional

from pydantic import BaseModel
from pydantic.utils import GetterDict


class TreatmentServiceGetter(GetterDict):
    def get(self, key: str, default: Any = None) -> Any:
        if key in {
            "id",
            "service_type",
            "expected_date",
            "executed_date",
            "start_time",
            "end_time",
            "observations",
            "customer_id",
            "headquarter_id",
            "invoice_id",
        }:
            return getattr(self._obj.service, key)
        else:
            return super(TreatmentServiceGetter, self).get(key, default)


class TreatmentService(BaseModel):
    id: Optional[str]
    service_type: Optional[str]
    expected_date: Optional[datetime]
    executed_date: Optional[datetime]
    start_time: Optional[time]
    end_time: Optional[time]
    observations: Optional[str]
    customer_id: Optional[int]
    headquarter_id: Optional[int]
    invoice_id: Optional[int]

    class Config:
        orm_mode = True
        getter_dict = TreatmentServiceGetter


class ServiceTreatmentGetter(GetterDict):
    def get(self, key: str, default: Any = None) -> Any:
        if key in {
            "id",
            "name",
            "cost",
            "frequency",
        }:
            return getattr(self._obj.treatment, key)
        else:
            return super(ServiceTreatmentGetter, self).get(key, default)


class ServiceTreatment(BaseModel):
    id: Optional[int]
    name: Optional[str]
    cost: Optional[int]
    frequency: Optional[str]
    status: Optional[str]
    observations: Optional[str]

    class Config:
        orm_mode = True
        getter_dict = ServiceTreatmentGetter

