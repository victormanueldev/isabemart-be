from typing import Optional, List
from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app import crud, schemas, models

router = APIRouter()


@router.post("/", response_model=schemas.Customer)
def create_customer_with_headquarter(
        *,
        db: Session = Depends(deps.get_db),
        customer_in: schemas.CustomerCreate,
        current_user: models.User = Depends(deps.get_current_user),
) -> Optional[models.Customer]:
    """
    Create new customer with headquarter.
    """
    customer = crud.customer.get_by_document_id(db, document_id=customer_in.document_id)
    if customer:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    customer = crud.customer.create_with_headquarter(db, obj_in=customer_in)
    return customer


@router.get('/', response_model=List[schemas.Customer])
def get_customers_all(
        *,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(deps.get_current_user),
) -> List[models.Customer]:
    customers = crud.customer.get_multi(db)
    return customers


@router.patch('/', response_model=schemas.Customer)
def update_customer(
        *,
        db: Session = Depends(deps.get_db),
        customer_in: schemas.CustomerUpdate,
        curren_user: models.User = Depends(deps.get_current_user)
) -> models.Customer:
    customer = crud.customer.get(db, customer_in.id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    customer = crud.customer.update(db=db, obj_in=customer_in, db_obj=customer)
    return customer


@router.delete('/{customer_id}', response_model=schemas.Customer)
def delete_customer(
        *,
        db: Session = Depends(deps.get_db),
        customer_id: int,
        curren_user: models.User = Depends(deps.get_current_user)
):
    customer = crud.customer.get(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    customer = crud.customer.remove(db=db, id=customer_id)
    return customer
