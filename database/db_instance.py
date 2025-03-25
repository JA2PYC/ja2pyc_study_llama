import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv
import threading
import json

# 환경 변수 로드
load_dotenv()

# .env 파일에서 DB 설정 로드, 없으면 기본값 사용
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "llmaquarium")

# SQLAlchemy Database URL 생성
DATABASE_URL_DEFAULT = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/"
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

STATUS_FILE = "db_status.json"


# DB 상태 저장
def save_status(error_message=None):
    status = {"db_error": error_message}
    with open(STATUS_FILE, "w") as f:
        json.dump(status, f)


class Database:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(Database, cls).__new__(cls)
                    cls._instance._init_db()
        return cls._instance

    # DB 초기화
    def _init_db(self):
        try:
            self._create_database_if_not_exists()

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
            error_message = f"DB 연결실패 : {str(e)}"
            save_status(error_message)
            self.engine = None
            self.SessionLocal = None

    def _create_database_if_not_exists(self):
        try:
            engine = create_engine(DATABASE_URL_DEFAULT)
            with engine.connect() as conn:
                conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))
                conn.commit()

            engine = create_engine(DATABASE_URL)
            with engine.connect() as conn:
                conn.execute(
                    text(
                        """
                    CREATE TABLE IF NOT EXISTS users (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        email VARCHAR(100) UNIQUE NOT NULL
                    );
                    """
                    )
                )
                conn.commit()

                result = conn.execute(text("SELECT COUNT(*) FROM users"))
                count = result.scalar() or 0
                if count == 0:
                    conn.execute(
                        text(
                            "INSERT INTO users (name, email) VALUES ('admin', 'admin@llmaquarium.com');"
                        )
                    )
                    conn.commit()
        except OperationalError as e:
            save_status(f"DB 생성 실패 : {str(e)}")

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


# 전역적으로 사용할 수 있도록 인스턴스 생성
db_instance = Database()
