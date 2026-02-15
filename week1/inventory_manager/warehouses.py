from products import product_details
warehouse_locations = {"warehouse_A", "warehouse_B", "warehouse_C"}

def display_product_location():
    print("\n \n \n Location of all products:")
    for product in product_details:
        print(f"{product_details[product]['name']} is in {product_details[product]['location']}")

