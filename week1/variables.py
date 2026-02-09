firstName = 'Vignesh'
lastName = 'Potharaj'
print(firstName == lastName)
### 10 Coding Interview Questions (Beginner Level)
# 1.Create variables for name, age, height and print them in one sentence.
name = "vignesh"
age = 10
height = 5.5
print(f"my name is {name}, im {age} years old and my height is {height} feet")
# 2.Write code to calculate and print area of rectangle (length × width).
def area_of_rect(l,w):
    return (l*w)
print(area_of_rect(4,8))
# 3.Ask user for two numbers and print their sum, difference, product.
num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number"))
print("the sum is", num1 + num2)
print("the difference is", num1 - num2)
print("the product is", num1 * num2)
# 4.Create variables price and tax_rate, calculate final price with tax.
price = 100
tax_rate = 10
final_price = price + (price * tax_rate/100)
print(final_price)
# 5.Swap values of two variables without using a third variable.
price, tax_rate = tax_rate, price
print(price, tax_rate)
# 6.Convert temperature from Celsius to Fahrenheit (F = C × 9/5 + 32).
def C2F(C):
    return (C * 9/5) + 32
print(C2F(33))
# 7.Calculate simple interest: principal × rate × time / 100.
def simple_interest(principal,rate,time):
    return ((principal * rate * time)/ 100)
print(simple_interest(100,10,10))
# 8.Take user input for radius and calculate circle area (pi ≈ 3.14).
radius = int(input("enter the radius of the circle"))
pi = 3.14
area = (pi*(radius*radius))
print(area)
# 9.Create variables for hours and rate, calculate weekly pay.
hours = 9
rate = 10
print((hours*rate)*5)
# 10.Ask user for three numbers and print the largest one.
num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number"))
num3 = int(input("enter 3rd number"))

print(max(num1, num2, num3))