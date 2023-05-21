from datetime import datetime, time

from sqlalchemy import Column, Integer, String, DateTime, Time, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Service(Base):
    id = Column(Integer, primary_key=True, index=True)
    service_type = Column(String, index=True, nullable=False)
    expected_date = Column(DateTime, nullable=False)
    executed_date = Column(DateTime, nullable=False)
    start_time = Column(Time, nullable=True)
    end_time = Column(Time, nullable=True)
    observations = Column(String, nullable=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    headquarter_id = Column(Integer, ForeignKey("headquarter.id"))
    invoice_id = Column(Integer, ForeignKey("invoice.id"))

    customer = relationship("Customer", foreign_keys=[customer_id], back_populates="services", passive_deletes=True)

    invoice = relationship("Invoice", foreign_keys=[invoice_id], back_populates="services", passive_deletes=True)

    users = relationship("ServiceUser", cascade="all, delete-orphan", back_populates="service")

    treatments = relationship("ServiceTreatment", cascade="all, delete-orphan", back_populates="service")

    def __init__(
        self,
        service_type: str,
        expected_date: datetime,
        executed_date: datetime,
        start_time: time,
        end_time: time,
        observations: str,
    ):
        self.service_type = service_type
        self.expected_date = expected_date
        self.executed_date = executed_date
        self.start_time = start_time
        self.end_time = end_time
        self.observations = observations
