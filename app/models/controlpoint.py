from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class ControlPoint(Base):
    id = Column(Integer, nullable=False, primary_key=True, index=True)
    name = Column(String, nullable=False)
    status = Column(String, nullable=False)
    observations = Column(String, nullable=False)

    area_id = Column(Integer, ForeignKey("area.id"))
    area = relationship("Area", back_populates="control_points", passive_deletes=True)

    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship("Customer", back_populates="control_points")

    headquarter_id = Column(Integer, ForeignKey("headquarter.id"))
    headquarter = relationship("Headquarter", back_populates="control_points")
