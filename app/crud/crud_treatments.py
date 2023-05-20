from typing import Optional, List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.treatment import Treatment
from app.schemas.treatment import TreatmentCreate, TreatmentUpdate


class CRUDTreatment(CRUDBase[Treatment, TreatmentCreate, TreatmentUpdate]):
    def get_by_ids(self, db: Session, ids: List[int]) -> Optional[List[Treatment]]:
        return db.query(self.model).filter(Treatment.id.in_(ids)).all()


treatments = CRUDTreatment(Treatment)
