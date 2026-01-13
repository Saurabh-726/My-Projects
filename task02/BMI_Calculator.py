def calculate_bmi():
    print("Welcome to the Python BMI Calculator ")
    
    try:
        weight = float(input("Enter your weight in kg: "))
        height_cm = float(input("Enter your height in cm: "))
        
        height_m = height_cm / 100
        
        bmi = weight / (height_m ** 2)
        
        bmi = round(bmi, 2)
        
        print(f"\nYour BMI is: {bmi}")
        
        if bmi < 18.5:
            print("Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            print("Category: Normal weight")
        elif 25 <= bmi < 29.9:
            print("Category: Overweight")
        else:
            print("Category: Obese")
            
    except ValueError:
        print("Error: Please enter valid numerical values.")

if __name__ == "__main__":
    calculate_bmi()