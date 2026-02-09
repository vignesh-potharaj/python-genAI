product_details = {
    "product1" : { 
        "name": "football",
        "product_id": 1,
        "location": "warehouse_A",
        "rating": 4.5,
        "supplier": "SUP1",
        "stock": 2
    },
    "product2" : {
        "name": "basketball",
        "product_id": 2,
        "location": "warehouse_B",
        "rating": 4.8,
        "supplier": "SUP2",
        "stock": 7
    },
    "product3" : {
    "name": "volleyball",
    "product_id": 3,
    "location": "warehouse_C",
    "rating": 5,
    "supplier": "SUP3",
    "stock": 0
    }
}
inventory_history = [100, 50, 75, 120, 45]
transaction_history = []
supplier_cred = ("SUP1","SUP2") 

warehouse_locations = {"warehouse_A", "warehouse_B", "warehouse_C"}


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
                                        8. Exit
                """)

            try:    
                action = int(input("eneter the listed number to perform the respective action (1 to 8)"))
                if(action == 1):
                    display_inventory_history()
                elif(action == 2):
                    upadte_transactions()
                elif(action == 3):
                    update_inventory()
                elif(action == 4):
                    display_product_location()
                elif(action == 5):
                    check_stock_levels()
                elif(action == 6):
                    calculate_reorder_levels()
                elif(action == 7):
                    update_product_details()
                elif(action == 8):
                    print("exiting.....\n \n \n")
                    break
                else:
                    print("enter a value within thye range 1 to 8")
            except ValueError:
                print("enter a valid number")
    
def display_inventory_history():
    print("Diplaying Inventory History")
    print(inventory_history)
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


if __name__ == "__main__":
    select_action()

# forgot to add supplier creds