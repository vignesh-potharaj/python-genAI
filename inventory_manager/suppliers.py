# check if a supplier is in our suppplier database
from .products import product_details
supplier_cred = ("SUP1", "SUP2", "SUP3") 

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
