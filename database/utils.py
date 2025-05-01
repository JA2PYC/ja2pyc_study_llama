# database/utils.py
import json
from .config import STATUS_FILE


def save_status(error_message=None):
    status = {"db_error": error_message}
    with open(STATUS_FILE, "w") as f:
        json.dump(status, f)
