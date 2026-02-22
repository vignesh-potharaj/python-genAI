from .products import product_details
from .utils import get_yes_no
my_cart = []
shipping_charges = lambda cart: int(cart * 0.1) # lambda function


def view_cart(cart=None): #deafault parameter
    if cart is None:
        cart = ["product1"]
    total = 0
    for item in cart:
        print(f"name : {product_details[item]['name']} \n    price: {product_details[item]['price']}")
        total = total +  product_details[item]['price']
    print(f"Total value of the cart is {total}")
    print(f"Shipping charges are {shipping_charges(total)}")
    total = total + shipping_charges(total)
    print(f"Final Amount is {total}")

def add_to_cart():
    for product in product_details:
        print(f"{product}\n name: {product_details[product]['name']} \n price: {product_details[product]['price']}")

    product_pointer = input("enter which product to add to cart\n")
    my_cart.append(product_pointer)
    print("cart successfully updated")
    view_cart(my_cart)
    get_yes_no("do you want to add more?(y or n) ")
    if get_yes_no == 'n':
        return
    else:
        add_to_cart() #recursive function

def check_out():
    pass
