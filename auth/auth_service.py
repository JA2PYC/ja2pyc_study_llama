# auth/auth_service.py

from database.database_manager import DatabaseManager as _db_manager
from database.entities import UserEntity
from .password_hasher import verify_password
from .jwt_token import create_access_token

class AuthService:
    def __init__(self):
        self.db= _db_manager
    
    def login(self, login_id:str, password:str)->UserEntity | None:
        session = self.db.get_session()
        user = session.query(UserEntity).filter_by(login_id=login_id).first()
        
        if user and verify_password(password, user.password):
            return user
        return None
    
    @staticmethod
    def login_static(login_id: str, password: str):
        session = _db_manager.get_session()
        with session as db:
            user = db.query(UserEntity).filter_by(login_id=login_id).first()
            if not user or not verify_password(password, user.password):
                return None  # 로그인 실패

            if not user.is_active:
                return None  # 비활성화 계정

            return create_access_token({"user_id": user.id, "is_admin": user.is_admin})
