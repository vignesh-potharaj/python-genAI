# A BMI(Body Mass Index) calculator is a tool that
# estimates whether a person’s weight is healthy for their height.
# formula - bmi = weight/(height)^2
# scale- Underweight: BMI less than 18.5
        # Normal weight: 18.5 – 24.9
        # Overweight: 25 – 29.9
        # Obesity: 30 or greater

def BMI(weight, height):
    return weight/(height*height)

weight = float(input("enter your weight"))
height = float(input("enter your height"))
print(BMI(weight,height))