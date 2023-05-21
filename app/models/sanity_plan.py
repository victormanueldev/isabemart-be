from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class SanityPlan(Base):
    id = Column(Integer, nullable=False, primary_key=True, index=True)
    visits_qty = Column(Integer, nullable=False)
    frequency = Column(String, nullable=False)

    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship("Customer", back_populates="sanity_plans")
