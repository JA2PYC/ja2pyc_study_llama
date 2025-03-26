import logging
import os
from logging.handlers import RotatingFileHandler

# 로그 저장 폴더 (없으면 자동 생성)
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "log")
os.makedirs(LOG_DIR, exist_ok=True)

def get_logger(name, filename, level=logging.INFO):
    """파일 로그 설정"""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        log_file = os.path.join(LOG_DIR, filename)
        
        handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=5, encoding="utf-8")
        handler.setLevel(level)

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)

        logger.addHandler(handler)

    return logger
