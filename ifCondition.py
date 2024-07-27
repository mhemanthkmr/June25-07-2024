india = ["mumbai", "bangalore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

userInput = input("Enter the city name: ").lower() 

if userInput in india:
    print("The city is in India")
elif userInput in pakistan:
    print("The city is in Pakistan")
elif userInput in bangladesh:
    print("The city is in Bangladesh")
else:
    print("No such city in list")

# Two cities
india = ["mumbai", "bangalore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

userInput_1 = input("Enter the first city name: ").lower()
userInput_2 = input("Enter the second city name: ").lower()

if userInput_1 in india and userInput_2 in india:
    print("Both cities are in India")
elif userInput_1 in pakistan and userInput_2 in pakistan:
    print("Both cities are in Pakistan")
elif userInput_1 in bangladesh and userInput_2 in bangladesh:
    print("Both cities are in Bangladesh")
else:
    print("They do not belong to the same country")

