# check if a supplier is in our suppplier database
from .products import*
supplier_cred = ("SUP1", "SUP2", "SUP3") 

def verify_supplier():
    for product in products:
        print(product)

    product_pointer = input("""
        enter which product to verify
    """)
    if products[product_pointer]['supplier'] in supplier_cred:
        print(f"""
        supplier found in database
            VERIFIED SUPPLIER-{products[product_pointer]['supplier']}
""")
