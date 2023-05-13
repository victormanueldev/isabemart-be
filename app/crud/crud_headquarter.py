from typing import List
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.headquarter import Headquarter
from app.models.customer import Customer
from app.schemas.headquarter import HeadquarterCreate, HeadquarterUpdate


class CRUDHeadquarter(CRUDBase[Headquarter, HeadquarterCreate, HeadquarterUpdate]):
    def create_with_customer(self, db: Session, *, obj_in: HeadquarterCreate, customer: int) -> Headquarter:
        # Encode incoming data into a json structure and return it as dict
        obj_in_data = jsonable_encoder(obj_in)
        # Pass the structure to create a SQLAlchemy model instance
        db_obj = self.model(**obj_in_data, customer_id=customer)
        # Save the model
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_with_customer(self, db: Session) -> List[Headquarter]:
        return db.query(self.model).join(Customer).all()


headquarter = CRUDHeadquarter(Headquarter)
