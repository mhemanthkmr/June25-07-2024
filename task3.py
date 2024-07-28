def calculate_bmi(weight, height):
    # Calculate BMI using the formula: weight / (height * height)
    bmi = weight / (height ** 2)

    # Determine the BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obesity"

    return bmi, category

# Example usage:
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi, category = calculate_bmi(weight, height)

print(f"Your BMI is: {bmi:.2f}")
print(f"You are categorized as: {category}")
