from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas, models
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.Treatment)
def save_treatment(
    *,
    db: Session = Depends(deps.get_db),
    treatment_in: schemas.TreatmentCreate,
    current_user: models.User = Depends(deps.get_current_user),
) -> models.Treatment:
    treatment = crud.treatments.create(db=db, obj_in=treatment_in)
    return treatment


@router.get("/", response_model=List[schemas.Treatment])
def get_all(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> List[models.Treatment]:
    treatments = crud.treatments.get_multi(db)
    return treatments
