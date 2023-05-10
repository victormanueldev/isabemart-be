from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .headquarter import Headquarter  # noqa: F401


class Customer(Base):
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(String, index=True, nullable=False)
    customer_type = Column(String, nullable=False)
    commercial_name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    city = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    headquarters = relationship('Headquarter', back_populates='customer', cascade="all, delete-orphan")

    areas = relationship('Area', back_populates='customer', cascade="all, delete-orphan")
