# database/__init__.py
print("[INIT] ℹ️ database 패키지 초기화")

from .connector import db_client, DatabaseClient

__all__ = ["db_client", "DatabaseClient"]
