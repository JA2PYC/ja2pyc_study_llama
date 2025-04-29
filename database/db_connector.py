import threading
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

from .db_config import DATABASE_URL
from .db_init import create_database_and_tables
from .db_status import save_status

class DatabaseClient:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(DatabaseClient, cls).__new__(cls)
                    cls._instance._init_db()
        return cls._instance

    def _init_db(self):
        try:
            create_database_and_tables()

            self.engine = create_engine(
                DATABASE_URL,
                pool_size=10,
                max_overflow=20,
                pool_recycle=1800,
                pool_pre_ping=True,
            )
            self.SessionLocal = sessionmaker(
                bind=self.engine, autocommit=False, autoflush=False
            )
            save_status(None)
        except OperationalError as e:
            error_message = f"DB 연결 실패: {str(e)}"
            save_status(error_message)
            self.engine = None
            self.SessionLocal = None

    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def get_session(self):
        if self.SessionLocal:
            return self.SessionLocal()
        else:
            return None

# 전역 인스턴스
db_client = DatabaseClient()
