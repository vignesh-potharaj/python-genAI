import json
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "inventory_log.json")
class Logger:
    @staticmethod
    def load_data():
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as log_file:
                data = json.load(log_file)
                return data
        return {}
    @staticmethod
    def log_inventory(action, value):
        log = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "value": value
        }

        try:
            Logger.load_data()
            if Logger.load_data():
                data = Logger.load_data()
            else:
                    data = []
            data.append(log)
            with open(LOG_FILE, "w") as log_file:
                json.dump(data, log_file, indent=4)
            print("transaction log added")
        except Exception as e:
            print("Error caught", e)
