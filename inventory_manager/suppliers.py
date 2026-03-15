# check if a supplier is in our suppplier database
from .products import*
supplier_cred = ("SUP1", "SUP2", "SUP3") 

def verify_supplier(inventory):
    inventory.display_products()
    product_pointer = int(input("""
        enter which product to verify
    """))
    product = products[product_pointer - 1]
    if product.supplier in supplier_cred:
        print(f"""
        supplier found in database
        product {product.name} VERIFIED SUPPLIER-{product.supplier}
""")
