from .log import*
inventory_history = [100, -30, 50, 75, -56, 120, 45, -325]
transaction_history = []
supplier_cred = ("SUP1","SUP2","SUP3") 

warehouse_locations = {"warehouse_A", "warehouse_B", "warehouse_C"}



class Product:
    def __init__(self, name, product_id, location, rating, supplier, stock, price):
        self.name = name
        self.product_id = product_id
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
    def update_product_details(self):
        print('Products and their details \n')
        for product in products:
            print(product.name)
        product_pointer = input("""
                        enter which product to update
        """)
        update = input(f"""
                        Select what info to update
                        {product.items}
        """)
        value = input("""
                        Enter the Value
        """)
        products[product_pointer][update] = value
        print(f"""
                        Updated details of the product
                        {products[product_pointer]}
    """)


    def check_stock_levels(self):
            print("\n \n \n Stock levels for all products:")

            for product in products:
                if(products[product].stock <= 5):
                    print(f"""
                                ALERT!!
                                LOW {products[product].name} STOCK is {products[product]['stock']} """)
                else:
                    print(f"""
                                Stock levels are fine 
                                {products[product]['name']} STOCK is {products[product]['stock']}""")

    def calculate_reorder_levels(self):
            print("\n \n \n The products we need to reorder are:")
            for product in products:
                if(products[product]["stock"] <= 5):

                    print(f"""
                                We need to order more {5 - (products[product]['stock'])}  {products[product]['name']}s  """)
                else:
                    print(f"""
                                Stock levels are fine for {products[product]['name']}
                                STOCK is {products[product]['stock']}""")           
    def update_transactions(self):
        global transaction_history
        action = int(input("enter transaction (+ for credit && - for debit"))
        transaction_history.append(action) 
        print("updated transactions",transaction_history)

    # Build a list that captures only the positive stock 
    # additions from your inventory history.
    def view_only_positive_stock(self):
        positive_stock = [ stock for stock in inventory_history if stock >= 1 ]
        print(positive_stock)


product1 = Product(name = "football",
        product_id = 1,
        location = "warehouse_A",
        rating = 4.5,
        supplier = "SUP1",
        stock = 2,
        price = 459)
product2 = Product( 
        name = "basketball",
        product_id = 2,
        location = "warehouse_B",
        rating = 4.8,
        supplier = "SUP2",
        stock = 7,
        price = 999)

product3 = Product(
        name = "volleyball",
        product_id = 3,
        location ="warehouse_C",
        rating = 5,
        supplier = "SUP3",
        stock = 0,
        price = 1229)

products =[product1, product2, product3]