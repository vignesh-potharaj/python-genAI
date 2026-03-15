from .products import*
warehouse_locations = {"warehouse_A", "warehouse_B", "warehouse_C"}

def display_product_location():
    print("\n \n \n Location of all products:")
    for product in products:
        print(f"{product.name} is in {product.location}")

