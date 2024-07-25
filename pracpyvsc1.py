while True :
    print("""
         Please select your options below :
            1) Calculate BMI
            2) Exit
    """)
    choice = int(input("Enter your choice: "))
    if(choice == 1) :
        
        name = input("Enter your name : ")
        weight = float(input("Please enter weight in (KG) : "))
        height = float(input("Please enter height in (CM) : "))
        heightMeter = height / 100
        bmi = weight / heightMeter ** 2
        if(bmi < 18.4):
            print(f"{name} Under Weight")
        elif (bmi > 18.4 and bmi < 24.9):
            print(f"{name} Normal Weight")
        elif (bmi > 24.9 and bmi < 39.9):
            print(f"{name} Over Weight")
        else:
            print("Obese")

    elif (choice == 2):
        print("Program Successfully Executed")
        break
    else:
        ("Invalid Choices")            