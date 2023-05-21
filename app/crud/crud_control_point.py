from app.crud.base import CRUDBase
from app.models.controlpoint import ControlPoint
from app.schemas.control_point import ControlPointCreate, ControlPointUpdate


class CRUDControlPoint(CRUDBase[ControlPoint, ControlPointCreate, ControlPointUpdate]):
    pass


control_point = CRUDControlPoint(ControlPoint)
