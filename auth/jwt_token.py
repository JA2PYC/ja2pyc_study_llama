# auth/jwt_token.py

import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key"  # 환경변수로 빼는 것을 추천
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_minutes: int = 60):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
