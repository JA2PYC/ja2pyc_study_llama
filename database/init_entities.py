# init_entities.py
from .database_manager import DatabaseManager as DB_Manager
from .entities.base import Base

# Set Entity
from . import entities

def init_entities():
    Base.metadata.create_all(bind=DB_Manager.get_engine())