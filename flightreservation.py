def sign_up(credentials):
    print("\nSign Up for the Flight Reservation System")
    while True:
        username = input("Choose a username: ")
        if username in credentials:
            print("Username already exists. Please try a different one.")
        else:
            password = input("Choose a password: ")
            credentials[username] = password
            print("Sign-up successful!")
            return

def login(credentials):
    print("\nLogin to the Flight Reservation System")
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if credentials.get(username) == password:
            print("Login successful!")
            return
        else:
            print("Invalid credentials. Please try again.")

def choose_flight():
    flights = {
        1: {"name": "Flight A", "time": "8:00 AM", "price": 150},
        2: {"name": "Flight B", "time": "12:00 PM", "price": 200},
        3: {"name": "Flight C", "time": "6:00 PM", "price": 250}
    }
    while True:
        print("\nAvailable Flights:")
        for key, value in flights.items():
            print(f"{key}: {value['name']} - {value['time']} - ${value['price']}")
        
        choice = int(input("Choose a flight by entering the corresponding number: "))
        if choice in flights:
            selected_flight = flights[choice]
            print(f"You have chosen: {selected_flight['name']} at {selected_flight['time']} for ${selected_flight['price']}")
            return selected_flight['price']
        else:
            print("Invalid choice. Please try again.")

def payment(price):
    methods = {
        1: "Credit Card",
        2: "Debit Card",
        3: "PayPal"
    }
    while True:
        print("\nPayment Methods:")
        for key, value in methods.items():
            print(f"{key}: {value}")
        
        choice = int(input("Choose a payment method by entering the corresponding number: "))
        if choice in methods:
            print(f"Payment of ${price} successful with: {methods[choice]}")
            return
        else:
            print("Invalid choice. Please try again.")

def main():
    credentials = {}
    
    while True:
        choice = input("\nDo you want to sign up or login? (signup/login): ").strip().lower()
        if choice == "signup":
            sign_up(credentials)
        elif choice == "login":
            login(credentials)
        else:
            print("Invalid choice. Please enter 'signup' or 'login'.")
            continue
        
        price = choose_flight()
        payment(price)
        print("\nThank you for booking with us!")
        break

if __name__ == "__main__":
    main()