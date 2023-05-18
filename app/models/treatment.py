from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Treatment(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    cost = Column(Integer, nullable=False)
    frequency = Column(String, nullable=False)

    services = relationship('ServiceTreatment', cascade='all, delete-orphan', back_populates='treatment')
