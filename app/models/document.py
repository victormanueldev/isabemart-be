from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Document(Base):
    id = Column(Integer, primary_key=True, index=True)
    document_type = Column(String, nullable=False, default="Certificacion")
    upload_datetime = Column(DateTime, nullable=False)
    status = Column(String, nullable=False, default="Vigente")

    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship("Customer", back_populates="documents", passive_deletes=True)
