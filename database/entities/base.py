# database/entities/base.py
from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.orm import declarative_base

# Entity Base
# Base = declarative_base()
Base: DeclarativeMeta = declarative_base()