while True : #runs continuously
    print("""
          Please enter the options below:
             1.Calculate BMI
             2.Exit
          """)
    choice= int(input("Enter your choice:"))
    if(choice == 1):
        print("")
        name=input("Enter your name:")
        weight=float(input("Enter your weight in kg:"))
        height=float(input("Enter you  height  in cm:"))
        height_in_meter=height/100
        bmi=weight/(height_in_meter**2)
        if(bmi<18.5):
            print("Under weight")
        elif(bmi>18.5 and bmi<24.9):
            print("Normal")
        elif(bmi>24.9 and bmi<39.9):
            print("Over weight")
        else:
            print("obese")
    elif(choice == 2):
        print("Program executed successfully")     
        break
    else:
        print("Invalid choice")