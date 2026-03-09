from .products import*
from .utils import print_decorator
from .log import*
inventory_history = [100, -30, 50, 75, -56, 120, 45, -325]
transaction_history = []
supplier_cred = ("SUP1","SUP2","SUP3") 

warehouse_locations = {"warehouse_A", "warehouse_B", "warehouse_C"}
class Inventory:
    @print_decorator
    @staticmethod
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