from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .customer import Customer  # noqa: F401


class Headquarter(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    neighborhood = Column(String, nullable=True)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship("Customer", back_populates="headquarters", foreign_keys=[customer_id], passive_deletes=True)
