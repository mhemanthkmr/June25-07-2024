while True:
    print("""Enter your Choice: 
          1. open irctc
          2. serach trains
          3. ticket booking
          4. view details
          5
          4. Money transfer
          5. Exit""")
    
choice = input("enter the your choice")
if choice == 1:
print("welcome irctc ")

elif choice == 2:
        source = input("Enter source city: ")
        destination = input("Enter destination city: ")
        print(f"Searching train from {source} to {destination}...")
elif choice == 3:
        name = input("Enter your name: ")
        source = input("Enter source city: ")
        destination = input("Enter destination city: ")
        date = input("Enter travel date (YYYY-MM-DD): ")
        print(f"Booking ticket for {name} from {source} to {destination} on {date}...")

elif choice ==4:
elif choice == 3:
        booking_id = input("Enter your booking ID: ")
        print(f"Viewing details for booking ID {booking_id}...")
        # Add logic to retrieve and display booking details here
    
    elif choice == 4:
        booking_id = input("Enter your booking ID: ")
        print(f"Cancelling booking ID {booking_id}...")
        # Add logic to cancel booking here
    
    elif choice == 5:
        print("Program successfully executed")
        break
    
    else:
        print("Invalid choice")
2. Sbookin
        

