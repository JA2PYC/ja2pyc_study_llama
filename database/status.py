import json

STATUS_FILE = "db_status.json"


def save_status(error_message=None):
    status = {"db_error": error_message}
    with open(STATUS_FILE, "w") as f:
        json.dump(status, f)
