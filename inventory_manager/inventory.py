from .products import*
from .utils import print_decorator
from .log import*
inventory_history = [100, -30, 50, 75, -56, 120, 45, -325]
transaction_history = []
supplier_cred = ("SUP1","SUP2","SUP3") 

warehouse_locations = {"warehouse_A", "warehouse_B", "warehouse_C"}
@print_decorator
def display_inventory_history(self):
    print("Diplaying Inventory History")
    return (inventory_history) ## return function    


def update_inventory(self):
    action = input("select an action(add or deduct)")
    value = int(input(f"enter the value to {action}"))
    if(action == "add"):
        inventory_history.append(value)
        print("The updated inventory is",inventory_history)
    elif(action == "deduct"):
        inventory_history.remove(value, inventory_history.index(value))
        print("The updated inventory is",inventory_history)
    log_inventory(action, value)
