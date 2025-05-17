# database/database_connector.py
from .database_client import DatabaseClient

_db_client = None

def get_db_client():
    global _db_client 
    if _db_client is None:
        _db_client = DatabaseClient()
    return _db_client

def get_engine():
    return get_db_client().get_engine()

def get_session():
    return get_db_client().get_session()
        