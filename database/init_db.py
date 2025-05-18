from .database_manager import get_engine
from .entities.base import Base
from .entities import *

def init_db():
    Base.metadata.create_all(bind=get_engine())