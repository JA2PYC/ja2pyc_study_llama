# Python Server 실행용
# run.py
print("[INFO] ℹ️ Run Server")

from dashboard.app import app

# 가상환경 활성화 후
# gunicorn -w 4 -b 127.0.0.1:8000 run:app
