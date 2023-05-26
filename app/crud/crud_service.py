from typing import List, Any, Union, Dict

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.associations.service_treatment import ServiceTreatment
from app.models.associations.service_user import ServiceUser
from app.models.customer import Customer
from app.models.invoice import Invoice
from app.models.service import Service
from app.models.treatment import Treatment
from app.models.user import User
from app.schemas.service import ServiceCreate, ServiceUpdate


class CRUDService(CRUDBase[Service, ServiceCreate, ServiceUpdate]):
    def get_multi_paginated(
            self, db: Session, *, skip: int = 0, limit: int = 100, status: str
    ) -> List[Service]:
        return db.query(self.model).filter(self.model.status == status).offset(skip).limit(limit).all()

    def create_service(
            self,
            db: Session,
            treatments_db: List[Treatment],
            customer_db: Customer,
            user_db: User,
            *,
            obj_in: ServiceCreate,
    ) -> Service:
        obj_data = jsonable_encoder(obj_in)
        service_db = self.model(
            service_type=obj_data["service_type"],
            expected_date=obj_data["expected_date"],
            executed_date=obj_data["executed_date"],
            start_time=obj_data["start_time"],
            end_time=obj_data["end_time"],
            observations=obj_data["observations"],
        )
        invoice_db = Invoice()
        invoice_db.calculate_total_invoiced(treatments=treatments_db)
        db.add(invoice_db)
        db.commit()
        db.refresh(invoice_db)
        for treatment in treatments_db:
            service_db.treatments.append(ServiceTreatment(treatment))
        service_db.invoice_id = invoice_db.id
        service_db.users.append(ServiceUser(user_db))
        service_db.customer_id = customer_db.id
        if len(customer_db.headquarters) > 0:
            service_db.headquarter_id = customer_db.headquarters[0].id
        db.add(service_db)
        db.commit()
        db.refresh(service_db)
        return service_db

    def update_service(self, db: Session, *, db_obj: Service, obj_in: Union[ServiceUpdate, Dict[str, Any]],
                       treatments: List[Treatment], user: User):
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db_treatments = []
        for treatment in treatments:
            db_treatments.append(ServiceTreatment(treatment))
        db_obj.treatments = db_treatments
        db_user = ServiceUser(user)
        db_obj.user = db_user
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


service = CRUDService(Service)
