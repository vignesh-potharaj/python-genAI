from .suppliers import *
from .warehouses import *
from .cart import *
from .products import *
from .storage import*
inventory = Inventory()


def run_menu(title, actions):
    while True:
        print(f"\n----- {title} -----")

        for key, value in actions.items():
            print(f"{key}. {value[0]}")

        try:
            choice = int(input("Select an option: "))

            if choice not in actions:
                print("Invalid option")
                continue

            if actions[choice][1] is None:
                break

            actions[choice][1]()

        except ValueError:
            print("Enter a valid number")



# MAIN MENU 
def exit_app():
    Storage.save_inventory(products)
    print("Inventory saved. Closing application...")
    exit()


main_actions = {
    1: ("Products", lambda: run_menu("Product Menu", product_actions)),
    2: ("Inventory", lambda: run_menu("Inventory Menu", inventory_actions)),
    3: ("Cart", lambda: run_menu("Cart Menu", cart_actions)),
    4: ("Save and Exit", exit_app) # Call the helper instead of 'None'
}

# PRODUCT MENU 

product_actions = {
    1: ("View Product Summary", lambda: products[0].get_product_summary()),
    2: ("Update Product Details", lambda: products[0].update_product_details()),
    3: ("Update Stock", lambda: products[0].update_stock()),
    4: ("Display Product Info", lambda: products[0].display_info()),
    5: ("Get Total Products", Product.get_total_products),
    6: ("Add Product", inventory.add_product),
    7: ("Find Product", inventory.find_product),
    8: ("List All Products", inventory.list_all_products),
    9: ("Back", None)
}


# INVENTORY MENU 

inventory_actions = {
    1: ("Display Inventory History", Inventory.display_inventory_history),
    2: ("Update Inventory", Inventory.update_inventory),
    3: ("Display Product Location", display_product_location),
    4: ("Check Stock Levels", inventory.check_stock_levels),
    5: ("Calculate Reorder Levels", inventory.calculate_reorder_levels),
    6: ("View Positive Stock Transactions", Inventory.view_only_positive_stock),
    7: ("Verify Supplier", lambda: verify_supplier(inventory)),
    8: ("Back", None)
}


# CART MENU 

cart_actions = {
    1: ("View Cart", lambda: Cart.view_cart(my_cart)),
    2: ("Add To Cart", add_to_cart),
    3: ("Checkout", check_out),
    4: ("Back", None)
}


def main():
    # 1. Try to load saved data
    loaded_data = Storage.load_inventory()
    
    if loaded_data:
        # 2. If we found data, clear the defaults and use the saved list
        products.clear()
        products.extend(loaded_data)
        print(f"Loaded {len(products)} products from file.")
    else:
        print("No save file found. Using default products.")

    run_menu("Inventory Management System", main_actions)

if __name__ == "__main__":
    main()