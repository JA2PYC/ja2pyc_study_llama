# database/entities/base.py
from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.orm import declarative_base

# Entity Base
Base: DeclarativeMeta = declarative_base()
# Base = declarative_base()