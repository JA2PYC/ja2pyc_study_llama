# User Entity
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, func
from sqlalchemy.orm import relationship

# SQLAlchemy Base
from .base import Base


class UserEntity(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login_id = Column(String(128), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    user_name = Column(String(128), nullable=False)
    # email = Column(String, unique=True, nullable=False)
    admin_memo = Column(Text)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    last_login_at = Column(DateTime)
    auth_accounts = relationship(
        "UserAuthAccountEntity", backref="user", cascade="all, delete-orphan"
    )
