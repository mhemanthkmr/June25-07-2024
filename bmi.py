#bmi BMI = kg/m2 
#bmr - BMR for Men = 66.47 + (13.75 * weight [kg]) + (5.003 * size [cm]) − (6.755 * age [years])
# BMR for Women = 655.1 + (9.563 * weight [kg]) + (1.85 * size [cm]) − (4.676 * age [years])
while True: 
    print("""
        1. BMI calculator
        2. BMR calculator
        3. Exit""")
    choice = int(input("Enter choice: "))


    if (choice ==1): #BMI calculator
    #Underweight = <18.5
    # Normal weight = 18.5–24.9
    # Overweight = 25–29.9
    # Obesity = BMI of 30 or greater

            Name = input("Enter name: ")
            Height = float(input("Enter height in m: "))
            Weight = float (input("Enter weight in kg: "))
            BMI = Weight/(Height)*2
            if (BMI <= 18.5):
                print(Name,"- Your BMI is Underweight")
            elif (BMI >=18.5 and BMI <=24.9):
                print(Name ,"- Your BMI is Normal weight") 
            elif (BMI >=25 and BMI <=29.9):
                print(Name,"- Your BMI is Overweight") 
            else:
                print(Name, "- Your BMI is Obesity")  

    elif (choice ==2): # BMR calculator

            Name = input("Enter name: ")
            Gender = input("Enter gender: ")
            Age = int(input("Enter age: "))
            Height = float(input("Enter height in cm: "))
            Weight = float (input("Enter weight in kg: "))
            if (Gender == "male"):
                BMR = 88.362 + (13.397 * Weight) + (4.799 * Height) - (5.677 * Age)
                print(Name, "- Your BMR value for Men: ",BMR)
            elif(Gender == "female"):
                BMR = 447.593 + (9.247 * Weight) + (3.098 * Height) -(4.330 * Age )
                print(Name, "- Your BMR value for Women: ",BMR)

            else:
                print("Invalid input")
    elif (choice ==3):
        print("Exit")
        break

    else:
        print("Invalid choice")

