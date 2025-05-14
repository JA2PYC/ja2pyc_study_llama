from .connector import engine
from .connector import Base
# from .connector import DatabaseClient
from .entities import user_entity

def init_db():
    # engine = DatabaseClient.get_engine()
    Base.metadata.create_all(bind=engine)