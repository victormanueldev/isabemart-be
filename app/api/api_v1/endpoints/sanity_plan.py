from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas, models
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.SanityPlan])
def get_all(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> List[models.SanityPlan]:
    sanity_plans = crud.sanity_plan.get_multi(db)
    return sanity_plans


@router.post("/", response_model=schemas.SanityPlan)
def save_sanity_plan(
    *,
    db: Session = Depends(deps.get_db),
    sanity_plan_in: schemas.SanityPlanCreate,
    current_user: models.User = Depends(deps.get_current_user),
) -> models.SanityPlan:
    sanity_plan = crud.sanity_plan.create(db, obj_in=sanity_plan_in)
    return sanity_plan


@router.patch("/{sanity_plan_id}", response_model=schemas.SanityPlan)
def update_sanity_plan(
    *,
    db: Session = Depends(deps.get_db),
    sanity_plan_id: int,
    sanity_plan_in: schemas.SanityPlanUpdate,
    current_user: models.User = Depends(deps.get_current_user),
) -> models.SanityPlan:
    sanity_plan = crud.sanity_plan.get(db, id=sanity_plan_id)
    if not sanity_plan:
        raise HTTPException(status_code=404, detail="Sanity plan not found")
    sanity_plan_updated = crud.sanity_plan.update(db, db_obj=sanity_plan, obj_in=sanity_plan_in)
    return sanity_plan_updated


@router.delete("/{sanity_plan_id}", response_model=bool)
def delete_sanity_plan(
    *,
    db: Session = Depends(deps.get_db),
    sanity_plan_id: int,
    current_user: models.User = Depends(deps.get_current_user),
) -> bool:
    sanity_plan = crud.sanity_plan.get(db, id=sanity_plan_id)
    if not sanity_plan:
        raise HTTPException(status_code=404, detail="Sanity plan not found")
    return crud.sanity_plan.remove(db, id=sanity_plan_id)
