# Retrieve last 3 transactions with negative indexing
user_transactions = [1500.00, -200.50, -45.99, 3000.00, -150.75, -899.99,10]
last_three = user_transactions[::3]  # Negative indexing for last elements
print(f"Last 3 transactions: {last_three}")

product_details = {
    "name": "football",
    "stock": 2
}

if(product_details["stock"] < 5):
    print(f"""
                ALERT!!
                LOW {product_details['name']} STOCK is {product_details['stock']} """)
