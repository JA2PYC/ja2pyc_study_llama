# User Entity
from sqlalchemy import Column, Integer, String

# SQLAlchemy Base
from .base import Base

class UserEntity(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
