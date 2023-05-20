from typing import Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.customer import Customer
from app.models.headquarter import Headquarter
from app.schemas.customer import CustomerCreate, CustomerUpdate


class CRUDCustomer(CRUDBase[Customer, CustomerCreate, CustomerUpdate]):
    def get_by_document_id(self, db: Session, *, document_id: str) -> Optional[Customer]:
        return db.query(self.model).filter(Customer.document_id == document_id).first()

    def get_with_headquarter(self, db: Session, *, customer_id: int, headquarter_id: int) -> Optional[Customer]:
        return (
            db.query(self.model)
            .join(Headquarter)
            .filter(Customer.id == customer_id, Headquarter.id == headquarter_id)
            .first()
        )

    def create_with_headquarter(self, db: Session, *, obj_in: CustomerCreate) -> Customer:
        obj_customer = jsonable_encoder(obj_in)
        obj_headquarter = None
        if "headquarter" in obj_customer:
            obj_headquarter = obj_customer.pop("headquarter")
        db_customer = self.model(**obj_customer)
        if obj_headquarter:
            db_headquarter = Headquarter(**obj_headquarter)
            db_customer.headquarters.append(db_headquarter)
        db.add(db_customer)
        db.commit()
        db.refresh(db_customer)
        return db_customer


customer = CRUDCustomer(Customer)
