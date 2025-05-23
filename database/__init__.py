# database/__init__.py
# from .database_client import DatabaseClient
from .database_manager import DatabaseManager as db_manager
from .mock_connector import mock_db_client, MockDatabaseClient
from .init_entities import init_entities

__all__ = [
    # "DatabaseClient",
    "db_manager",
    "mock_db_client",
    "MockDatabaseClient"
]

init_entities()