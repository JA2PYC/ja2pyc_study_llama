from .connector import get_engine
from .entities.base import Base
from .entities import user_entity

def init_db():
    Base.metadata.create_all(bind=get_engine())