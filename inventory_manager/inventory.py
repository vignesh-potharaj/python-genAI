from .products import*
from .utils import print_decorator
from .log import*
inventory_history = [100, -30, 50, 75, -56, 120, 45, -325]
transaction_history = []
supplier_cred = ("SUP1","SUP2","SUP3") 

warehouse_locations = {"warehouse_A", "warehouse_B", "warehouse_C"}
class Inventory:
        #add products via terminal
    def add_product(self):
        print("Available products")
        self.display_products(self)
        print("--------Add New Product--------")
        name = input("Enter the Name of the product: ")
        SKU = input("Enter the SKU of the product: ")
        while not Product.validate_sku(SKU):
            SKU = input("Enter a valid SKU (Example: EL-1001): ")
        location = input("Enter the Location of the product: ")
        rating = int(input("Enter the Rating of the product: "))
        supplier = input("Enter the Supplier of the product: ")
        stock = int(input("Enter the Stock of the product: "))
        price = int(input("Enter the Price of the product: "))
        new_product = Product(name, SKU, location, rating, supplier, stock, price)
        products.append(new_product)
        new_product.display_info()
    def display_products(self):
        for index, product in enumerate(products):
            print(f"{index + 1} {product}")
    def find_product(self, SKU = None):
        if SKU is None:
            SKU =  input("enter the SKU to search any product(ex: EL-1001): ")
            while not Product.validate_sku(SKU):
                SKU = input("Enter a valid SKU (Example: EL-1001): ")
        for product in products:
            if product.SKU == SKU:
                product.display_info(product=product)
                return
        print("No product matched for the given SKU")
    def list_all_products(self):
        for product in products:
            product.display_info(product=product)
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


    @staticmethod
    @print_decorator
    def display_inventory_history():
        print("Diplaying Inventory History")
        return (inventory_history) ## return function    

    @staticmethod
    def update_inventory():
        action = input("select an action(add or deduct)")
        value = int(input(f"enter the value to {action}"))
        if(action == "add"):
            inventory_history.append(value)
            print("The updated inventory is",inventory_history)
        elif(action == "deduct"):
            inventory_history.remove(value, inventory_history.index(value))
            print("The updated inventory is",inventory_history)
        log_inventory(action, value)
    @staticmethod
    def update_transactions():
        global transaction_history
        action = int(input("enter transaction (+ for credit && - for debit"))
        transaction_history.append(action) 
        print("updated transactions",transaction_history)

    @staticmethod
    def view_only_positive_stock():
        positive_stock = [ stock for stock in inventory_history if stock >= 1 ]
        print(positive_stock)