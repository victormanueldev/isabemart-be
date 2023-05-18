from typing import List
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.headquarter import Headquarter
from app.models.invoice import Invoice
from app.models.user import User
from app.models.customer import Customer
from app.models.treatment import Treatment
from app.models.service import Service
from app.models.associations.service_treatment import ServiceTreatment
from app.models.associations.service_user import ServiceUser
from app.schemas.service import ServiceCreate, ServiceUpdate


class CRUDService(CRUDBase[Service, ServiceCreate, ServiceUpdate]):
    def create_service(
            self,
            db: Session,
            treatments_db: List[Treatment],
            customer_db: Customer,
            user_db: User,
            *,
            obj_in: ServiceCreate
    ) -> Service:
        obj_data = jsonable_encoder(obj_in)
        service_db = self.model(
            service_type=obj_data['service_type'],
            expected_date=obj_data['expected_date'],
            executed_date=obj_data['executed_date'],
            start_time=obj_data['start_time'],
            end_time=obj_data['end_time'],
            observations=obj_data['observations'],
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
        db.add(service_db)
        db.commit()
        db.refresh(service_db)
        return service_db


service = CRUDService(Service)
