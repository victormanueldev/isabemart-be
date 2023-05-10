from typing import Optional
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.customer import Customer
from app.models.headquarter import Headquarter
from app.schemas.customer import CustomerCreate, CustomerUpdate


class CRUDCustomer(CRUDBase[Customer, CustomerCreate, CustomerUpdate]):

    def get_by_document_id(self, db: Session, *, document_id: str) -> Optional[Customer]:
        return db.query(Customer).filter(Customer.document_id == document_id).first()

    def create_with_headquarter(self, db: Session, *, obj_in: CustomerCreate) -> Customer:
        obj_customer = jsonable_encoder(obj_in)
        obj_headquarter = obj_customer.pop('headquarter')
        db_customer = self.model(**obj_customer)
        if obj_headquarter:
            db_headquarter = Headquarter(**obj_headquarter)
            db_customer.headquarters.append(db_headquarter)
        db.add(db_customer)
        db.commit()
        db.refresh(db_customer)
        return db_customer


customer = CRUDCustomer(Customer)


