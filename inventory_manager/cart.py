from .products import*
from .utils import get_yes_no
my_cart = []
shipping_charges = lambda cart: int(cart * 0.1) # lambda function

class Cart:
    def view_cart(self, cart=None): #deafault parameter
        if cart is None:
            cart = [product1]
        total = 0
        for product in cart:
            print(f"name : {product.name} \nprice: {product.price}")
            total = total +  product.price
        print(f"Total value of the cart is {total}")
        print(f"Shipping charges are {shipping_charges(total)}")
        total = total + shipping_charges(total)
        print(f"Final Amount is {total}")

def add_to_cart():
    for index, product in enumerate(products):
        print(f"{index + 1} name: {product.name} \n price: {product.price}")
    while True:
        try:
            product_pointer = int(input("enter which product to add to cart\n"))
            if product_pointer <= len(products):
                my_cart.append(product_pointer)
                print("cart successfully updated")
                Cart.view_cart(my_cart)
            else:
                print(f"enter a value between 1 and {len(products)}")
        except Exception as e:
            print("error caught", e)
        get_yes_no("do you want to add more?(y or n) ")
        if get_yes_no == 'n':
            return
        else:
            add_to_cart() #recursive function

def check_out():
    pass
