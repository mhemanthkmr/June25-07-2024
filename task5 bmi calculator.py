#task 5 BMI calculator
height=float(input("Enter your height in cm:"))
weight=float(input("Enter your weight in kg:"))

bmi=weight/(height/100)**2
print("height:",height)
print("weight:",weight)

print("your bmi is:",bmi)

if bmi<=18.5:
    print("you are under weight")
elif bmi<=24.9:
    print("you are healthy")
elif bmi<=29.9:
    print("you are over weight")
else:
    print("you are obese")