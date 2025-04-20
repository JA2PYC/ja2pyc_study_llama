from sqlalchemy import create_engine
from config.models import Base, Setting

engine = create_engine("sqlite:///config/settings.db", echo=True)
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# 설정 삽입
session.merge(Setting(key="DEBUG", value="false"))
session.merge(Setting(key="APP_NAME", value="UserApp"))
session.merge(Setting(key="MAX_CONNECTIONS", value="20"))
session.commit()
session.close()
