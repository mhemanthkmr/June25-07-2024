
print("""choose your option         
                1.Type 'start' to start the program.
                2.Type 'end' to close the program.""")
while True:      
        option=input("Enter your option :")
        if(option=='start'):
            print("BMI CALCULATOR")
            name=input("Enter your Name :")
            height=float(input("Enter your Height:"))
            weight=float(input("enter your Weight:"))

            h=height/100
            bmi=weight/(h*h)

            print("BMI count :",bmi)
            if(bmi<18.4):
                 print(f"BMI count {bmi} is low. Increase your weight.")
            elif(bmi>18.4 and bmi<24.9):
                 print(f"BMI count {bmi} is normal.")
            else:
                 print(f"BMI count {bmi} is high. Reduce your weight.")

        elif(option=='end'):
            print("program executed successfully.")
            break
