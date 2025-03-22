import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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


class Database:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(Database, cls).__new__(cls)
                    cls._instance.engine = create_engine(
                        DATABASE_URL,
                        pool_size=10,  # 유지할 최대 연결 수
                        max_overflow=20,  # 초과 허용할 추가 연결 수
                        pool_recycle=1800,  # 연결 재사용 주기 (초)
                        pool_pre_ping=True,  # 연결 유지 체크
                    )
                    cls._instance.SessionLocal = sessionmaker(
                        bind=cls._instance.engine, autocommit=False, autoflush=False
                    )
        return cls._instance

    # DB 상태 저장
    def save_status(error_message=None):
        status = {"db_error": error_message}
        with open(STATUS_FILE, "w") as f:
            json.dum(status, f)

    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()


# 전역적으로 사용할 수 있도록 인스턴스 생성
db_instance = Database()
