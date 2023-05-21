from app.crud.base import CRUDBase
from app.models.sanity_plan import SanityPlan
from app.schemas.sanity_plan import SanityPlanCreate, SanityPlanUpdate


class CRUDSanityPlan(CRUDBase[SanityPlan, SanityPlanCreate, SanityPlanUpdate]):
    pass


sanity_plan = CRUDSanityPlan(SanityPlan)
