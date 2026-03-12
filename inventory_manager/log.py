import json
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INVENTORY_FILE = os.path.join(BASE_DIR, "inventory_log.json")
PRODUCT_FILE = os.path.join(BASE_DIR, "product_.json")
class Logger:
    @staticmethod
    def load_data(FILE):
        if os.path.exists(FILE):
            with open(FILE, "r") as file:
                data = json.load(file)
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
            Logger.load_data(INVENTORY_FILE)
            if Logger.load_data(INVENTORY_FILE):
                data = Logger.load_data(INVENTORY_FILE)
            else:
                    data = []
            data.append(log)
            with open(INVENTORY_FILE, "w") as inventory_file:
                json.dump(data, inventory_file, indent=4)
            print("transaction log added")
        except Exception as e:
            print("Error caught", e)
    @staticmethod
    def log_action(action, product_name, new_value):
        log = {
            "time_stamp": datetime.now().isoformat(),
            "action": action,
            "product_name": product_name,
            "new_value": new_value
        }
        try:
            Logger.load_data(PRODUCT_FILE)
            if Logger.load_data(PRODUCT_FILE):
                data = Logger.load_data(PRODUCT_FILE)
            else:
                data = []
            data.append(log)
            with open(PRODUCT_FILE, 'w') as product_file:
                json.dump(data, product_file,  indent = 4)
            print("product log sucessfully added")
        except Exception as e:
            print("error caught:", e)
