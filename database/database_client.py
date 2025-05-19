# database/database_client.py
import threading

# SQL Alchemy
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

# Abstract Class
from .abstract_database_client import AbstractDatabaseClient

# Settings
from .config import DATABASE_URL, DATABASE_URL_DEFAULT, DB_NAME
from .utils import save_status


class DatabaseClient(AbstractDatabaseClient):
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance._init_db()
        return cls._instance

    def _init_db(self):
        try:
            self._create_database_if_not_exists()
            self.engine = create_engine(DATABASE_URL, pool_pre_ping=True)
            self.SessionLocal = sessionmaker(
                bind=self.engine, autocommit=False, autoflush=False
            )
            save_status(None)
        except OperationalError as e:
            save_status(f"DB 연결 실패: {e}")
            self.engine = None
            self.SessionLocal = None

    def _create_database_if_not_exists(self):
        try:
            # DB 생성
            engine = create_engine(DATABASE_URL_DEFAULT)
            with engine.connect() as conn:
                conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))
                conn.commit()

        except OperationalError as e:
            save_status(f"DB 생성 실패: {e}")

    def get_session(self):
        return self.SessionLocal()

    def get_engine(self):
        return self.engine

    def get_db(self):
        db = self.get_session()
        try:
            yield db
        finally:
            db.close()
