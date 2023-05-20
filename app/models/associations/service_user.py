from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.user import User


class ServiceUser(Base):
    service_id = Column(Integer, ForeignKey("service.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    service = relationship("Service", back_populates="users")
    user = relationship("User", back_populates="services")

    def __init__(self, user: User):
        self.user_id = user.id
