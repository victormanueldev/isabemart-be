from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_technician = Column(Boolean(), default=False)
    is_customer = Column(Boolean(), default=False)
    is_superuser = Column(Boolean(), default=False)
    color = Column(String, unique=True)
