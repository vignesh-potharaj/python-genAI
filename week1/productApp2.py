product_details = {
    "product1" : { 
        "name": "football",
        "product_id": 1,
        "location": "warehouse_A",
        "rating": 4.5,
        "supplier": "SUP1",
        "stock": 2,
        "price": 459
    },
    "product2" : {
        "name": "basketball",
        "product_id": 2,
        "location": "warehouse_B",
        "rating": 4.8,
        "supplier": "SUP2",
        "stock": 7,
        "price": 999
    },
    "product3" : {
    "name": "volleyball",
    "product_id": 3,
    "location": "warehouse_C",
    "rating": 5,
    "supplier": "SUP3",
    "stock": 0,
    "price": 1229

    }
}
inventory_history = [100, 50, 75, 120, 45]
transaction_history = []
supplier_cred = ("SUP1","SUP2") 

warehouse_locations = {"warehouse_A", "warehouse_B", "warehouse_C"}
my_cart = []
shipping_charges = lambda cart: int(cart * 0.1) # lambda function

def select_action():
    while True:
            print("""
                                        Welcome to Inventory & Data Structure Management
                                        1. Display Inventory History
                                        2. Update Transactions
                                        3. Update Inventory
                                        4. Display Product Location
                                        5. Check Stock Levels
                                        6. Calculate Reorder Levels
                                        7. Update Product Details
                                        8. Verify supplier
                                        9. View Cart
                                        10. Add to Cart
                                        11. View Cart
                                        12.exit
                """)
            action_map = {
                    1: display_inventory_history,
                    2: upadte_transactions,
                    3: update_inventory,
                    4: display_product_location,
                    5: check_stock_levels,
                    6: calculate_reorder_levels,
                    7: update_product_details,
                    8: verify_supplier,
                    9: lambda: view_cart(my_cart),
                    10: add_to_cart,
                    11: check_out
                }
            length_of_actions = len(action_map) + 1

            try:    
                action = int(input(f"eneter the listed number to perform the respective action (1 to {length_of_actions})"))
                if 1 <= action <= length_of_actions:
                    if action == length_of_actions:
                         break
                    action_map[action]()
                else:
                    print("enter a number between 1 and 8") 

            except ValueError:
                print("enter a valid number")
def print_decorator(func): #args, kwargs, decorators
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
    return wrapper
@print_decorator
def display_inventory_history():
    print("Diplaying Inventory History")
    return (inventory_history) ## return function    
def upadte_transactions():
    global transaction_history
    action = int(input("enter transaction (+ for credit && - for debit"))
    transaction_history.append(action)
    print("updated transactions",transaction_history)
def update_inventory():
    action = input("select an action(add or deduct)")
    if(action == "add"):
        value = int(input("enter the value to add"))
        inventory_history.append(value)
        print("The updated inventory is",inventory_history)
    elif(action == "deduct"):
        value = int(input("enter the value to add"))
        inventory_history.remove(value, inventory_history.index(value))
        print("The updated inventory is",inventory_history)
def display_product_location():
    print("\n \n \n Location of all products:")
    for product in product_details:
        print(f"{product_details[product]['name']} is in {product_details[product]['location']}")
def check_stock_levels():
        print("\n \n \n Stock levels for all products:")

        for product in product_details:
            if(product_details[product]["stock"] <= 5):
                print(f"""
                            ALERT!!
                            LOW {product_details[product]['name']} STOCK is {product_details[product]['stock']} """)
            else:
                print(f"""
                            Stock levels are fine 
                            {product_details[product]['name']} STOCK is {product_details[product]['stock']}""")

def calculate_reorder_levels():
        print("\n \n \n The products we need to reorder are:")
        for product in product_details:
            if(product_details[product]["stock"] <= 5):

                print(f"""
                            We need to order more {5 - (product_details[product]['stock'])}  {product_details[product]['name']}s  """)
            else:
                print(f"""
                            Stock levels are fine for {product_details[product]['name']}
                             STOCK is {product_details[product]['stock']}""")           


    
def update_product_details():
    print('Products and their details \n')
    for product in product_details:
        print(product)
    product_pointer = input("""
                     enter which product to update
    """)
    update = input(f"""
                     Select what info to update
                     {product_details[product_pointer]}
    """)
    value = input("""
                     Enter the Value
    """)
    product_details[product_pointer][update] = value
    print(f"""
                    Updated details of the product
                    {product_details[product_pointer]}
""")

# check if a supplier is in our suppplier database
def verify_supplier():
    for product in product_details:
        print(product)

    product_pointer = input("""
        enter which product to verify
    """)
    if product_details[product_pointer]['supplier'] in supplier_cred:
        print(f"""
        supplier found in database
            VERIFIED SUPPLIER-{product_details[product_pointer]['supplier']}
""")
        
def view_cart(cart=None): #deafault parameter
    if cart is None:
        cart = ["product1"]
    total = 0
    for item in cart:
        print(f"name : {product_details[item]['name']} \n    price: {product_details[item]['price']}")
        total = total +  product_details[item]['price']
    print(f"Total value of the cart is {total}")
    print(f"Shipping charges are {shipping_charges(total)}")
    total = total + shipping_charges(total)
    print(f"Final Amount is {total}")

def add_to_cart():
    pass

def check_out():
    pass



# Add an item 
if __name__ == "__main__":
    select_action()

# forgot to add supplier creds