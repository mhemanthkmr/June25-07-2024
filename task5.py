def check_sugar_level():
    # Ask user to enter fasting sugar level
    sugar_level = float(input("Enter your fasting sugar level: "))
    
    # Check if sugar level is normal, low, or high
    if sugar_level < 80:
        print("Sugar level is low.")
    elif sugar_level > 100:
        print("Sugar level is high.")
    else:
        print("Sugar level is normal.")

# Call the function to run the program
check_sugar_level()
