from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .customer import Customer  # noqa: F401
    from .headquarter import Headquarter  # noqa: F401


class Area(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    estimated_time = Column(String, nullable=False)
    incidence = Column(Boolean, nullable=False, default=False)
    activity_level = Column(String, nullable=False, default="No")

    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship("Customer", foreign_keys=[customer_id], back_populates="areas", passive_deletes=True)

    headquarter_id = Column(Integer, ForeignKey("headquarter.id"))
    headquarter = relationship("Headquarter", foreign_keys=[headquarter_id], passive_deletes=True)

    control_points = relationship("ControlPoint", back_populates="area", passive_deletes=True)
