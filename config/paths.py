import os
import sys

# PROJECT_ROOT = os.path.abspath(sys.path[0])
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

CONFIG_DIR = os.path.join(PROJECT_ROOT, "config")
LOG_DIR = os.path.join(PROJECT_ROOT, "log")
DATA_DIR = os.path.join(PROJECT_ROOT, "data")

# 폴더 생성 함수
def ensure_dirs():
    for path in [DATA_DIR, LOG_DIR]:
        os.makedirs(path, exist_ok=True)
