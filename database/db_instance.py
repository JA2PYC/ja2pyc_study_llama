from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import threading

DATABASE_URL = "sqlite:///example.db"  # MySQL: "mysql+pymysql://user:password@host/dbname"

class Database:
    _instance = None
    _lock = threading.Lock()  # 동시 접근 방지를 위한 Lock

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(Database, cls).__new__(cls)
                    cls._instance.engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)
                    cls._instance.SessionLocal = sessionmaker(bind=cls._instance.engine, autocommit=False, autoflush=False)
        return cls._instance

    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

# 전역적으로 사용할 수 있도록 인스턴스 생성
db_instance = Database()
