import json
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "inventory_log.json")

def log_inventory(action, value):
    log = {
        "timestamp": datetime.now().isoformat(),
        "action": action,
        "value": value
    }

    try:
        with open(LOG_FILE, "a") as log_file:
            json.dump(log, log_file)
            log_file.write("\n")
            print("transaction log added")
    except Exception as e:
        print("Error caught", e)