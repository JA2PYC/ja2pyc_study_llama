# database/mock_connector.py
from .abstract_database_client import AbstractDatabaseClient

class MockDatabaseClient(AbstractDatabaseClient):
    def get_session(self):
        print("💡 Mock session created")
        return MockSession()

    def get_db(self):
        yield self.get_session()

class MockSession:
    def query(self, *args, **kwargs):
        print("💡 Mock query called")
        return []

    def close(self):
        print("💡 Mock session closed")

mock_db_client = MockDatabaseClient()
