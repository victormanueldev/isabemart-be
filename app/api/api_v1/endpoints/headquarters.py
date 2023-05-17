from typing import Optional, List
from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app import crud, schemas, models

router = APIRouter()


@router.get('/', response_model=List[schemas.Headquarter])
def get_all(
        *,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(deps.get_current_user),
) -> List[models.Headquarter]:
    headquarters = crud.headquarter.get_with_customer(db=db)
    return headquarters


@router.post('/', response_model=schemas.Headquarter)
def save_headquarter(
        *,
        db: Session = Depends(deps.get_db),
        headquarter_in: schemas.HeadquarterCreate,
        current_user: models.User = Depends(deps.get_current_user)
) -> models.Headquarter:
    headquarter = crud.headquarter.create(db=db, obj_in=headquarter_in)
    return headquarter


@router.patch('/{headquarter_id}', response_model=schemas.Headquarter)
def update_headquarter(
        *,
        db: Session = Depends(deps.get_db),
        headquarter_id: int,
        headquarter_in: schemas.HeadquarterUpdate,
        current_user: models.User = Depends(deps.get_current_user),
) -> models.Headquarter:
    headquarter = crud.headquarter.get(db, id=headquarter_id)
    if not headquarter:
        raise HTTPException(status_code=404, detail="Headquarter not found")
    headquarter = crud.headquarter.update(db=db, db_obj=headquarter, obj_in=headquarter_in)
    return headquarter


@router.delete('/{headquarter_id}', response_model=bool)
def delete_headquarter(
        *,
        db: Session = Depends(deps.get_db),
        headquarter_id: int,
        current_user: models.User = Depends(deps.get_current_user),
) -> bool:
    headquarter = crud.headquarter.get(db, id=headquarter_id)
    if not headquarter:
        raise HTTPException(status_code=404, detail="Headquarter not found")
    headquarter = crud.headquarter.remove(db=db, id=headquarter_id)
    return headquarter


