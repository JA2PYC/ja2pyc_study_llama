from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()

class Setting(Base):
    __tablename__ = 'settings'
    key = Column(String, primary_key=True)
    value = Column(String)
