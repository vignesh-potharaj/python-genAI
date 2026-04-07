import os
import json
from .products import*
allowed_fields = [
    "name",
    "SKU",
    "location",
    "rating",
    "supplier",
    "stock",
    "price"
]
        
FILE_PATH = "products.json"

class Storage:
    def load_all(file_name, self):
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, 'r') as f:
                return json.load(f)
        return {} 
    @staticmethod      
    def save_data(product):
        data = Storage.load_all(FILE_PATH)
        filterred_product = {}
        for attr_name, attr_value in product.__dict__.items():
            if attr_name in allowed_fields:
                filterred_product[attr_name] = attr_value
        sku_key = product.SKU
        data[sku_key] = filterred_product
        with open(FILE_PATH, 'w') as f:
            json.dump(data, f)
    @staticmethod
    def load_data(SKU):
        data = Storage.load_all(FILE_PATH)
        if SKU in data:
            product_dict = data[SKU]
            return Product(**product_dict)
        else:
            print("Product not found")
            return None
