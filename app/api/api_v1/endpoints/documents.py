from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas, models
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Document])
def get_all(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> List[models.Document]:
    documents = crud.document.get_multi(db)
    return documents


@router.post("/", response_model=schemas.Document)
def save_document(
    *,
    db: Session = Depends(deps.get_db),
    document_in: schemas.DocumentCreate,
    current_user: models.User = Depends(deps.get_current_user),
) -> models.Document:
    document = crud.document.create(db, obj_in=document_in)
    return document


@router.patch("/{document_id}", response_model=schemas.Document)
def update_document(
    *,
    db: Session = Depends(deps.get_db),
    document_id: int,
    document_in: schemas.DocumentUpdate,
    current_user: models.User = Depends(deps.get_current_user),
) -> models.Document:
    document = crud.document.get(db, id=document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    document_updated = crud.document.update(db, db_obj=document, obj_in=document_in)
    return document_updated


@router.delete("/{document_id}", response_model=bool)
def delete_document(
    *,
    db: Session = Depends(deps.get_db),
    document_id: int,
    current_user: models.User = Depends(deps.get_current_user),
) -> bool:
    document = crud.document.get(db, id=document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return crud.document.remove(db, id=document_id)
