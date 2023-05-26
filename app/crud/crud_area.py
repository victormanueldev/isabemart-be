from typing import List
from app.crud.base import CRUDBase
from app.models.area import Area
from app.schemas.area import AreaCreate, AreaUpdate


class CRUDArea(CRUDBase[Area, AreaCreate, AreaUpdate]):

    def get_by_customer_headquarter(self, db, headquarter_id: int, customer_id: int) -> List[Area]:
        return db.query(self.model).filter(Area.headquarter_id == headquarter_id,
                                           Area.customer_id == customer_id).all()

    def get_by_customer(self, db, customer_id: int) -> List[Area]:
        return db.query(self.model).filter(Area.customer_id == customer_id).all()


area = CRUDArea(Area)
