from typing import List

from sqlalchemy import Column, Integer, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.treatment import Treatment


class Invoice(Base):
    id = Column(Integer, primary_key=True, index=True)
    total_invoiced = Column(Integer, nullable=False)
    is_paid = Column(Boolean, nullable=False, default=False)

    services = relationship("Service", back_populates="invoice")

    def calculate_total_invoiced(self, treatments: List[Treatment]) -> int:
        self.total_invoiced = sum(item.cost for item in treatments)
        return self.total_invoiced
