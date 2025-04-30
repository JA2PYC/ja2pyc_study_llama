from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

from .config import DATABASE_URL_DEFAULT, DATABASE_URL, DB_NAME
from .status import save_status

def create_database_and_tables():
    try:
        # DB 없으면 생성
        engine = create_engine(DATABASE_URL_DEFAULT)
        with engine.connect() as conn:
            conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))
            conn.commit()

        # users 테이블 생성
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

            # admin 유저 삽입
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
        save_status(f"DB 생성 실패: {str(e)}")
