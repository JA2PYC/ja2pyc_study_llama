# User Social Account Entity
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func

# SqlAlchemy Base
from .base import Base


class UserAuthAccountEntity(Base):
    __tablename__ = "user_auth_accounts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    provider = Column(String(128), nullable=False)
    provider_id = Column(String(255), nullable=False)
    email = Column(String(255))
    created_at = Column(DateTime, default=func.now())
