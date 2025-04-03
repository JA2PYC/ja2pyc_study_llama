import logging
import os
from logging.handlers import RotatingFileHandler

class Logger:
    _instances ={}
    LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "log")
    print("[TEST] ☑️ Logger - ",LOG_DIR)
    
    # Initialize Logger
    @classmethod
    def _initialize(cls, name, filename, level=logging.INFO):
        os.makedirs(cls.LOG_DIR, exist_ok=True)
        log_file = os.path.join(cls.LOG_DIR, filename)
        logger = logging.getLogger(name)
        logger.setLevel(level)
        
        if not logger.hasHandlers():
            handler = RotatingFileHandler(log_file,  maxBytes= 5 * 1024 * 1024, backupCount=5, encoding="UTF-8")
            handler.setLevel(level)
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            
        return logger
    
    # Singletone Logger
    @classmethod
    def get_logger(cls, name="app", filename="app.log", level =logging.INFO):
        if name not in cls._instances:
            cls._instances[name] = cls._initialize(name, filename, level)
            
        return cls._instances[name]
    

# # 로그 저장 폴더 (없으면 자동 생성)
# LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "log")
# print(LOG_DIR)
# # print(os.path.dirname())
# print(os.path.dirname(__file__))
# print(os.path.dirname(os.path.dirname(__file__)))
# os.makedirs(LOG_DIR, exist_ok=True)

# def get_logger(name, filename, level=logging.INFO):
#     """파일 로그 설정"""
#     logger = logging.getLogger(name)
#     logger.setLevel(level)

#     if not logger.handlers:
#         log_file = os.path.join(LOG_DIR, filename)
        
#         handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=5, encoding="utf-8")
#         handler.setLevel(level)

#         formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
#         handler.setFormatter(formatter)

#         logger.addHandler(handler)

#     return logger
