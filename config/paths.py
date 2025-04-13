import os
import sys

PROJECT_ROOT = os.path.abspath(sys.path[0])

LOG_DIR = os.path.join(PROJECT_ROOT, "log")
DATA_DIR = os.path.join(PROJECT_ROOT, "data")

print(sys.path)
print(PROJECT_ROOT)
print(LOG_DIR)
print(DATA_DIR)