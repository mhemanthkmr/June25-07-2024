height=float(input("Enter your height in cm:"))
weight=float(input("Enter your weight in kg:"))
bmi=weight/(height ** 2)
if bmi< 20.2:
    print("you are under weight.")
elif bmi < 28:
    print("you have normal weight")
else:
    print("you are slightly overweight")
    
    