from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas, models
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Service])
def get_all(
        *,
        skip: int = 0,
        limit: int = 100,
        status: str = None,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(deps.get_current_user),
) -> List[models.Service]:
    if status:
        services = crud.service.get_multi_paginated(db, skip=skip, limit=limit, status=status)
    else:
        services = crud.service.get_multi(db, skip=skip, limit=limit)
    return services


@router.get('/{service_id}', response_model=schemas.Service)
def get_by_id(
        *,
        db: Session = Depends(deps.get_db),
        service_id: int,
        current_user: models.User = Depends(deps.get_current_user),
) -> models.Service:
    service = crud.service.get(db, id=service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service


@router.post("/", response_model=schemas.Service)
def save_service(
        *,
        db: Session = Depends(deps.get_db),
        service_in: schemas.ServiceCreate,
        current_user: models.User = Depends(deps.get_current_user),
) -> Optional[models.Service]:
    customer = crud.customer.get_with_headquarter(
        db=db, customer_id=service_in.customer_id, headquarter_id=service_in.headquarter_id
    )
    if not customer and 'headquarter_id' in service_in:
        raise HTTPException(status_code=404, detail="Customer and Headquarter not found")
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    user_technician = crud.user.get(db=db, id=service_in.user_id)
    if not user_technician:
        raise HTTPException(status_code=404, detail="Technician not found")
    if not user_technician.is_technician:
        raise HTTPException(status_code=400, detail="Selected user is not a technician")
    treatments = crud.treatments.get_by_ids(db=db, ids=service_in.treatments)
    if len(treatments) == 0:
        raise HTTPException(status_code=404, detail="Treatments not found")
    service = crud.service.create_service(
        db=db, treatments_db=treatments, customer_db=customer, user_db=user_technician, obj_in=service_in
    )
    return service


@router.patch("/{service_id}", response_model=schemas.Service)
def update_service(
        *,
        db: Session = Depends(deps.get_db),
        service_id: int,
        service_in: schemas.ServiceUpdate,
        current_user: models.User = Depends(deps.get_current_user),
) -> Optional[models.Service]:
    service = crud.service.get(db, id=service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    user_technician = crud.user.get(db=db, id=service_in.user_id)
    if not user_technician:
        raise HTTPException(status_code=404, detail="Technician not found")
    treatments = crud.treatments.get_by_ids(db=db, ids=service_in.treatments)
    if len(treatments) == 0:
        raise HTTPException(status_code=404, detail="Treatments not found")
    service_updated = crud.service.update_service(db, db_obj=service, obj_in=service_in, treatments=treatments,
                                                  user=user_technician)
    return service_updated


@router.patch('/status/{service_id}', response_model=schemas.Service)
def update_status(
        *,
        db: Session = Depends(deps.get_db),
        service_id: int,
        service_in: schemas.ServiceUpdate,
        current_user: models.User = Depends(deps.get_current_user),
) -> models.Service:
    service = crud.service.get(db, id=service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return crud.service.update(db, obj_in=service_in, db_obj=service)


@router.delete("/{service_id}", response_model=bool)
def delete_service(
        *,
        db: Session = Depends(deps.get_db),
        service_id: int,
        current_user: models.User = Depends(deps.get_current_user),
) -> bool:
    service = crud.service.get(db, id=service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return crud.service.remove(db, id=service_id)
