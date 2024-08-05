while True:
    print("""
    please select your optionbelow:
        1. calculate BMI
        2. exit
    """)
    choice=int(input("please enter the option:"))
    if(choice==1):
        print("")
        name=input("Enter your name:")
        weight=float(input("Please enter weight in(KG)"))
        height=float(input("Please enter height in(CM)"))
        heightmeter=height/100
        bmi=weight/heightmeter**2
        if(bmi<18.4):
            print(f"{name},under weight")
        elif(bmi>18.4 and bmi<24.9):
            print(f"{name},normal")
        elif(bmi>24.9 and bmi<39.9):
            print(f"{name},over weight")
        else:
            print(f"{name},obesity")
    elif (choice==2):
        print("program sucessfully exceuted")
        break
    else:
        print("inavlid choice")

