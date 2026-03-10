from .log import*
inventory_history = [100, -30, 50, 75, -56, 120, 45, -325]
transaction_history = []
supplier_cred = ("SUP1","SUP2","SUP3") 

warehouse_locations = {"warehouse_A", "warehouse_B", "warehouse_C"}



class Product:
    def __init__(self, name, SKU, location, rating, supplier, stock, price):
        self.name = name
        self.SKU = SKU
        self.location = location
        self.rating = rating
        self.supplier = supplier
        self.stock = stock
        self.price = price
        self.product_summary = {
            "product name": name,
            "product rating": rating,
            "price of product": price
        }
        self.MIN_STOCK_LEVEL = 10
    def update_product_details(self):
        while True:
            try:
                print('enter which product to update\n')
                for index, product in enumerate(products):
                    print(f"{index + 1} {product.name}")
                product_index = int(input())
                product_index = product_index - 1
                product = products[product_index]
                self.display_info(product)
                break
            except Exception  as e:
                print("error caught,", e)
        while True:
            try:
                update = input(f"Select what info to update").strip()
                if update not in product.__dict__:
                    raise Exception("value entered is not present, try again")
                value = input("enetr the new value for the product").strip()
                original_type = type(getattr(product,update))  # it is going to return the original type
                value = original_type(value) # explicitly converting the value to the original type
                setattr(product, update, value)
                self.display_info(product)
                return
            except Exception  as e:
                print("error caught,", e)

    def check_stock_levels(self):
        print("\n \n \n Stock levels for all products:")
        for product in products:
            if(product.stock <= self.MIN_STOCK_LEVEL):
                print(f"""
                            ALERT!!
                            LOW {product.name} STOCK is {product.stock} """)
            else:
                print(f"""
                            Stock levels are fine 
                            {product.name} STOCK is {product.stock}""")

    def calculate_reorder_levels(self):
        print("\n \n \n The products we need to reorder are:")
        for product in products:
            if(product.stock <= self.MIN_STOCK_LEVEL):

                print(f"""
                            We need to order more {self.MIN_STOCK_LEVEL - (product.stock)}  {product.name}s  """)
            else:
                print(f"""
                            Stock levels are fine for {product.name}
                            STOCK is {product.stock}""")
    def get_product_summary(self):
        for index, product in enumerate(products):
            print(index + 1, product.name)
        product_pointer = int(input("select the product to view "))
        print(products[product_pointer - 1].product_summary)
    def update_stock(self):
        for index, product in enumerate(products):
            print(index + 1, product.name)
        product_pointer = int(input("select the product to update stock "))
        new_stock = int(input("enter the new stock"))
        setattr(products[product_pointer - 1], "stock", new_stock)
        print(f"{products[product_pointer - 1].name}'s stock is updated to {products[product_pointer - 1].stock}")
    def display_info(self, product = None):
        if product == None:
            for index, product in enumerate(products):
                print(index + 1, product.name)
            product_pointer = int(input("select the product to update stock "))
            product_pointer -= 1
            product = products[product_pointer]
        allowed_fields = [
            "name",
            "SKU",
            "location",
            "rating",
            "supplier",
            "stock",
            "price"
        ]
        print("------Product Info------")
        for key, value in product.__dict__.items():
            if key in allowed_fields:
                print(f"{key}: {value}")         
# Build a list that captures only the positive stock 
# additions from your inventory history.

product1 = Product(
        name = "football",
        SKU = "EL101",
        location = "warehouse_A",
        rating = 4.5,
        supplier = "SUP1",
        stock = 2,
        price = 459)
product2 = Product( 
        name = "basketball",
        SKU = "EL102",
        location = "warehouse_B",
        rating = 4.8,
        supplier = "SUP2",
        stock = 7,
        price = 999)

product3 = Product(
        name = "volleyball",
        SKU = "EL103",
        location ="warehouse_C",
        rating = 5,
        supplier = "SUP3",
        stock = 0,
        price = 1229)

products =[product1, product2, product3]