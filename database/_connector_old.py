# database/connector.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

class DatabaseClient:
    def __init__(self, db_url):
        """
        DatabaseClient 생성자
        :param db_url: 데이터베이스 접속 URL
        """
        self.db_url = db_url
        self.engine = None
        self.SessionLocal = None

    def connect(self):
        """
        데이터베이스 연결을 설정한다.
        """
        try:
            self.engine = create_engine(self.db_url, echo=True, future=True)
            self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
            print("✅ 데이터베이스 연결 성공")
        except SQLAlchemyError as e:
            print(f"❌ 데이터베이스 연결 실패: {e}")
            self.engine = None
            self.SessionLocal = None

    def get_session(self):
        """
        세션 객체를 가져온다.
        :return: 세션 객체 (SessionLocal 인스턴스)
        """
        if not self.SessionLocal:
            raise RuntimeError("SessionLocal이 설정되지 않았습니다. connect()를 먼저 호출하세요.")
        return self.SessionLocal()

    def close(self):
        """
        데이터베이스 연결을 종료한다.
        """
        if self.engine:
            self.engine.dispose()
            print("ℹ️ 데이터베이스 연결 종료 완료")
