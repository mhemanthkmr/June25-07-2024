account_balance = 1000  # Example starting balance

while True:
    print("""Enter your Choice: 
          1. Check Balance
          2. Deposit Money
          3. Withdraw Money
          4. Exit""")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print(f"Your current balance is ${account_balance}.")
    
    elif choice == 2:
        amount = float(input("Enter the amount to deposit: "))
        account_balance += amount
        print(f"Deposited ${amount}. New balance is ${account_balance}.")
    
    elif choice == 3:
        amount = float(input("Enter the amount to withdraw: "))
        if amount > account_balance:
            print("Insufficient funds.")
        else:
            account_balance -= amount
            print(f"Withdrew ${amount}. New balance is ${account_balance}.")
    
    elif choice == 4:
        print("Program successfully executed")
        break
    
    else:
        print("Invalid choice")
