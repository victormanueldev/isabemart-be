from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.treatment import Treatment


class ServiceTreatment(Base):
    service_id = Column(Integer, ForeignKey("service.id"), primary_key=True)
    treatment_id = Column(Integer, ForeignKey("treatment.id"), primary_key=True)
    status = Column(String, nullable=False, default="No iniciado")
    observations = Column(String, nullable=True)
    service = relationship("Service", back_populates="treatments")
    treatment = relationship("Treatment", back_populates="services")

    def __init__(self, treatment: Treatment):
        self.treatment = treatment
