from app.crud.base import CRUDBase
from app.models.area import Area
from app.schemas.area import AreaCreate, AreaUpdate


class CRUDArea(CRUDBase[Area, AreaCreate, AreaUpdate]):
    pass


area = CRUDArea(Area)
