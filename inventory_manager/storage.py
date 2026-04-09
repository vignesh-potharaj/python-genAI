import os
import json
from .products import Product # Import the class for rebuilding objects


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Use ONE file for everything
STORAGE_FILE = os.path.join(BASE_DIR, "products.json")

class Storage:
    @staticmethod
    def load_all(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}
        return {}

    @staticmethod
    def save_inventory(list_to_save):
        # Convert the objects into a dictionary format JSON can save
        data_to_write = {}
        for p in list_to_save:
            data_to_write[p.SKU] = {
                "name": p.name,
                "SKU": p.SKU,
                "location": p.location,
                "rating": p.rating,
                "supplier": p.supplier,
                "stock": p.stock,
                "price": p.price
            }
        
        # Write to the path you defined (STORAGE_FILE)
        with open(STORAGE_FILE, 'w') as f:
            json.dump(data_to_write, f, indent=4)
        
        print(f"--- Technical Log: Saved {len(list_to_save)} items to {STORAGE_FILE} ---")
    @staticmethod
    def load_inventory():
        # Load from the SAME file we saved to
        data = Storage.load_all(STORAGE_FILE)
        loaded_products = []
        for product_dict in data.values():
            # Turn dictionaries back into Product objects
            new_obj = Product(**product_dict)
            loaded_products.append(new_obj)
        return loaded_products