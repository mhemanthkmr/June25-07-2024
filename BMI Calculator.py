
weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    bmi_category = "Underweight"
elif bmi < 25:
    bmi_category = "Normal weight"
elif bmi < 30:
    bmi_category = "Overweight"
else:
    bmi_category = "Obesity"

print(f"Your BMI is: {bmi}")
print(f"You are considered: {bmi_category}")
