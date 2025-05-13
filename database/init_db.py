from .connector import engine
from .connector import Base
from .entities import user_entity

def init_db():
    Base.metadata.create_all(bind=engine)