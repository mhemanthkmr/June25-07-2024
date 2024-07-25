while True :
    print("""
          please choose a options in a given below:
               1. Love Calculator
               2. Simple Calculator
               3. BMI Calculator
               4. Exit
          """)
    


    choice = int(input("Enter your option no: "))
    if choice == 1 :
        
        def love_calculator(name1, name2):
           combined_names = name1.lower() + name2.lower()

           love_score = 0

           for character in combined_names:
                love_score += ord(character) - 96

           love_score = love_score % 101

           return love_score
           
        name1 = input("Enter your Lovely Name: ")
        name2 = input("Enter your Favourite Person Name: ")
  

        score = love_calculator(name1,name2)

        print(f"The love score for {name1} and {name2} is: {score}%")  

    elif choice == 2 :
        def simple_calculator(num1, num2):
            print("""
                Choose an operator no:
                  1. Addition
                  2. Subtraction
                  3. Multiplication
                  4. Division
                """)
            
            choice = int(input("Enter a given operator no: "))

            if choice == 1 :
                a = num1 + num2
                print(f"Your Addition value of {num1} and {num2} is : {a}")

            elif choice == 2 :
                s = num1 - num2
                print(f"Your Subtraction value of {num1} and {num2} is : {s}")

            elif choice == 3 :
                m = num1 * num2
                print(f"Your Multiplication value of {num1} and {num2} is : {m}")

            elif choice == 4 :
                d = num1 / num2
                print(f"Your Division value of {num1} and {num2} is : {d}")

            else :
                print("Invalid Syntax")

        num1 = float(input("Enter a first number : "))
        num2 = float(input("Enter a second number : "))

        simple_calculator(num1,num2)

    elif choice == 3 :

        name = input("Enter your name : ")
        weight = float(input("Please enter weight in (KG) : "))
        height = float(input("Please enter height in (CM) : "))

        heightMeter = height / 100

        bmi = weight / heightMeter ** 2

        if(bmi < 18.4):
            print(f"{name} You Are Under Weight")

        elif (bmi > 18.4 and bmi < 24.9):
            print(f"{name} You Are Normal Weight")

        elif (bmi > 24.9 and bmi < 39.9):
            print(f"{name} You Are Over Weight")

        else:
            print("Obese")

    elif choice == 4 :
        print("Your progress executed successfully. Thank You")
        break

    else :
        print("Invalid Syntax")    

