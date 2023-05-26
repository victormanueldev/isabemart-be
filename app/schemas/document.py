from datetime import datetime
from typing import Optional, Any

from pydantic import BaseModel


class DocumentBase(BaseModel):
    document_type: Optional[str]
    upload_datetime: Optional[datetime]
    status: Optional[str]
    url: Optional[str]
    name: Optional[str]
    customer_id: Optional[int]


class DocumentCreate(DocumentBase):
    pass


class DocumentUpdate(DocumentBase):
    pass


class DocumentInDBBase(DocumentBase):
    id: int

    class Config:
        orm_mode = True


class Document(DocumentInDBBase):
    customer: Optional[Any]
    pass
