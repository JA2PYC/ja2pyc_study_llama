from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.models import Setting
import config.settings as settings

DB_PATH = "sqlite:///config/settings.db"

def apply_db_settings():
    engine = create_engine(DB_PATH, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    db_settings = session.query(Setting).all()

    for item in db_settings:
        key = item.key
        value = item.value
        if hasattr(settings, key):
            current = getattr(settings, key)
            # 타입에 맞춰 안전하게 변환
            try:
                if isinstance(current, bool):
                    converted = value.lower() in ['true', '1', 'yes']
                elif isinstance(current, int):
                    converted = int(value)
                elif isinstance(current, float):
                    converted = float(value)
                else:
                    converted = value  # 문자열 등
                setattr(settings, key, converted)
            except Exception as e:
                print(f"[⚠️ 경고] 설정 '{key}' 값 변환 실패: {e}")

    session.close()
