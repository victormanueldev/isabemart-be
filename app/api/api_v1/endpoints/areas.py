from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas, models
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Area])
def get_all(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> List[models.Area]:
    areas = crud.area.get_multi(db=db)
    return areas


@router.post("/", response_model=schemas.Area)
def save_area(
    *,
    db: Session = Depends(deps.get_db),
    area_in: schemas.AreaCreate,
    current_user: models.User = Depends(deps.get_current_user),
) -> models.Area:
    area = crud.area.create(db=db, obj_in=area_in)
    return area


@router.patch("/{area_id}", response_model=schemas.Area)
def update_area(
    *,
    db: Session = Depends(deps.get_db),
    area_id: int,
    area_in: schemas.AreaUpdate,
    current_user: models.User = Depends(deps.get_current_user),
) -> models.Area:
    area = crud.area.get(db, id=area_id)
    if not area:
        raise HTTPException(status_code=404, detail="Area not found")
    area_updated = crud.headquarter.update(db=db, db_obj=area, obj_in=area_in)
    return area_updated


@router.delete("/{area_id}", response_model=bool)
def delete_area(
    *,
    db: Session = Depends(deps.get_db),
    area_id: int,
    current_user: models.User = Depends(deps.get_current_user),
) -> bool:
    area = crud.area.get(db, id=area_id)
    if not area:
        raise HTTPException(status_code=404, detail="Area not found")
    area_deleted = crud.area.remove(db=db, id=area_id)
    return area_deleted
