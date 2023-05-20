from pydantic import BaseModel


class InvoiceBase(BaseModel):
    total_invoiced: int
    is_paid: bool


class InvoiceInDBBase(InvoiceBase):
    id: int

    class Config:
        orm_mode = True


class Invoice(InvoiceBase):
    pass
