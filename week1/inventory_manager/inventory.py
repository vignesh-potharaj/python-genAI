from inventory_manager.products import*
from utils import print_decorator
inventory_history = [100, 50, 75, 120, 45]
transaction_history = []
supplier_cred = ("SUP1","SUP2","SUP3") 

warehouse_locations = {"warehouse_A", "warehouse_B", "warehouse_C"}

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

@print_decorator
def display_inventory_history():
    print("Diplaying Inventory History")
    return (inventory_history) ## return function    


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
def upadte_transactions():
    global transaction_history
    action = int(input("enter transaction (+ for credit && - for debit"))
    transaction_history.append(action)
    print("updated transactions",transaction_history)
