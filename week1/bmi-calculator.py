# A BMI(Body Mass Index) calculator is a tool that
# estimates whether a person’s weight is healthy for their height.
# formula - bmi = weight/(height)^2
# scale- Underweight: BMI less than 18.5
        # Normal weight: 18.5 – 24.9
        # Overweight: 25 – 29.9
        # Obesity: 30 or greater

def BMI(weight, height):
    result = round(weight/(height*height),2)
    if(result <= 18.5):
        return(f"""
                BMI is {(result)}
                SERIOUSLY UNDERWEIGHT!!!
                """)
    elif(result <= 24.9 and result > 18.5):   
        return(f"""
                BMI is {round(result)}
                NORMAL WEIGHT
                """)
    elif(result <= 30 and result > 24.9):
        return(f"""
                BMI is {round(result)}
                OVER WEIGHT!!!
                """)
    elif(result > 30):
        return(f"""
        BMI is {round(result)}
        !!! OBESE !!!
        """)



weight = float(input("enter your weight"))
height = float(input("enter your height"))
print(BMI(weight,height))