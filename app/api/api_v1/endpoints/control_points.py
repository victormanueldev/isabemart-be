from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas, models
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.ControlPoint])
def get_all(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> List[models.ControlPoint]:
    control_points = crud.control_point.get_multi(db)
    return control_points


@router.post("/", response_model=schemas.ControlPoint)
def save_control_point(
    *,
    db: Session = Depends(deps.get_db),
    control_point_in: schemas.ControlPointCreate,
    current_user: models.User = Depends(deps.get_current_user),
) -> models.ControlPoint:
    control_point = crud.control_point.create(db, obj_in=control_point_in)
    return control_point


@router.patch("/{control_point_id}", response_model=schemas.ControlPoint)
def update_control_point(
    *,
    db: Session = Depends(deps.get_db),
    control_point_id: int,
    control_point_in: schemas.ControlPointCreate,
    current_user: models.User = Depends(deps.get_current_user),
) -> models.ControlPoint:
    control_point = crud.control_point.get(db, id=control_point_id)
    if not control_point:
        raise HTTPException(status_code=404, detail="Control Point not found")
    control_point_updated = crud.control_point.update(db, db_obj=control_point, obj_in=control_point_in)
    return control_point_updated


@router.delete("/{control_point_id}", response_model=bool)
def delete_control_point(
    *,
    db: Session = Depends(deps.get_db),
    control_point_id: int,
    current_user: models.User = Depends(deps.get_current_user),
) -> bool:
    control_point = crud.control_point.get(db, id=control_point_id)
    if not control_point:
        raise HTTPException(status_code=404, detail="Control Point not found")
    return crud.control_point.remove(db, id=control_point_id)
