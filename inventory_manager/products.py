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
                print(product.__dict__)
                break
            except Exception  as e:
                print("error caught,", e)
        while True:
            try:
                update = input(f"""
                                Select what info to update
                """).strip()
                if update not in product.__dict__:
                    raise Exception("value entered is not present, try again")
                value = input("enetr the new value for the product").strip()
                original_type = type(getattr(product,update))  # it is going to return the original type
                value = original_type(value) # explicitly converting the value to the original type
                setattr(product, update, value)
                print(product.dict)
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

# Build a list that captures only the positive stock 
# additions from your inventory history.

product1 = Product(name = "football",
        SKU = 1,
        location = "warehouse_A",
        rating = 4.5,
        supplier = "SUP1",
        stock = 2,
        price = 459)
product2 = Product( 
        name = "basketball",
        SKU = 2,
        location = "warehouse_B",
        rating = 4.8,
        supplier = "SUP2",
        stock = 7,
        price = 999)

product3 = Product(
        name = "volleyball",
        SKU = 3,
        location ="warehouse_C",
        rating = 5,
        supplier = "SUP3",
        stock = 0,
        price = 1229)

products =[product1, product2, product3]