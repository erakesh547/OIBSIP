def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    try:
        # Get user input for weight and height
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        # Input validation (optional but recommended)
        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive numbers.")
            return
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Classify BMI
        category = classify_bmi(bmi)
        
        # Display the result
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    
    except ValueError:
        print("Error: Please enter valid numbers for weight and height.")

if __name__ == "__main__":
    main()
