1#bmi Calculater
while True:
    print("""Enter your Choice: 
          1. Calculate BMI 
          2. Exit""")
    choice=int(input("Enter your choice: "))
    if choice==1:
        name=input("Enter your name: ")
        weight=float(input("Enter your Weight: "))
        height=float(input("Enter your Height: "))
        heightMeter=height/100
        bmi=weight/heightMeter**2
        if bmi<18.5:
            print(f"Your BMI is {bmi}, UNDER WEIGHT ")
        elif bmi>=18.5 and bmi<=24.9:
            print(f"Your BMI is {bmi}, HEALTHY WEIGHT")
        elif bmi==25 and bmi<=29.9:
            print(f"Your BMI is {bmi}, OVER RANGE")
        else:
            print("Your are OBESE")
    elif choice==2:
        print("Program successfully executed")
        break
    else:
        print("Invalid choice")