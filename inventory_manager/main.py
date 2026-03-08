from .inventory import display_inventory_history, update_inventory
from .suppliers import verify_supplier
from .warehouses import display_product_location
from .cart import view_cart, add_to_cart, check_out, my_cart
from .inventory import*
from .products import*
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
                                        11. Check Out
                                        12. View only positive stock transactions
                                        13.exit
                """)
            action_map = {
                    1: display_inventory_history,
                    2: update_transactions,
                    3: update_inventory,
                    4: display_product_location,
                    5: lambda: products[0].check_stock_levels(),
                    6: lambda: products[0].calculate_reorder_levels(),
                    7: lambda: products[0].update_product_details(),
                    8: verify_supplier,
                    9: lambda: view_cart(my_cart),
                    10: add_to_cart,
                    11: check_out,
                    12: view_only_positive_stock
                }
            length_of_actions = len(action_map) + 1

            try:    
                action = int(input(f"eneter the listed number to perform the respective action (1 to {length_of_actions})"))
                if 1 <= action <= length_of_actions :
                    if action == length_of_actions:
                         break
                    action_map[action]()
                else:
                    print("enter a number between 1 and 8") 

            except ValueError:
                print("enter a valid number")


# Add an item 
if __name__ == "__main__":
    select_action()
