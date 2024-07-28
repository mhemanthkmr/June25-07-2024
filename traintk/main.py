from datetime import datetime

class RailwaySystem:
    def __init__(self):
        self.trains = []
        self.users = []
        self.reservations = []
        self.add_sample_trains()

    def add_sample_trains(self):
        self.add_train('101', 'chennai', 'madurai', '09:00 AM', 100)
        self.add_train('102', 'chennai', 'salem', '10:00 AM', 150)
        self.add_train('103', 'chennai', 'theni', '11:00 AM', 200)
        self.add_train('104', 'madurai', 'chennai', '12:00 PM', 120)

    def add_train(self, train_number, origin, destination, departure, seats):
        train = {
            'train_number': train_number,
            'origin': origin,
            'destination': destination,
            'departure': departure,
            'seats': seats,
            'booked_seats': []
        }
        self.trains.append(train)
        print(f"Train {train_number} from {origin} to {destination} at {departure} with {seats} seats added.")

    def register_user(self, username, password):
        for user in self.users:
            if user['username'] == username:
                print("Username already exists.")
                return
        new_user = {'username': username, 'password': password}
        self.users.append(new_user)
        print("User registered successfully.")

    def login_user(self, username, password):
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                print("Login successful.")
                return True
        print("Invalid username or password.")
        return False

    def book_ticket(self, username, train_number, passenger_name, passenger_age, from_place, to_place, departure_time, departure_date, seat_number):
        train_found = False
        for train in self.trains:
            print(f"Checking train {train['train_number']}:")
            print(f"  Origin: {train['origin']} == {from_place}")
            print(f"  Destination: {train['destination']} == {to_place}")
            print(f"  Departure Time: {train['departure']} == {departure_time}")
            
            if train['train_number'] == train_number and train['origin'] == from_place and train['destination'] == to_place and train['departure'] == departure_time:
                train_found = True
                if seat_number > train['seats'] or seat_number < 1:
                    print(f"Invalid seat number. Please choose a seat number between 1 and {train['seats']}.")
                    return
                if seat_number in train['booked_seats']:
                    print("Seat already booked.")
                    return
                train['booked_seats'].append(seat_number)
                reservation = {
                    'username': username,
                    'train_number': train_number,
                    'passenger_name': passenger_name,
                    'passenger_age': passenger_age,
                    'from_place': from_place,
                    'to_place': to_place,
                    'departure_time': departure_time,
                    'departure_date': departure_date,
                    'seat_number': seat_number
                }
                self.reservations.append(reservation)
                print("Ticket booked successfully.")
                return
        if not train_found:
            print("Train not found or details do not match.")

    def cancel_ticket(self, username, train_number, seat_number):
        for reservation in self.reservations:
            if reservation['username'] == username and reservation['train_number'] == train_number and reservation['seat_number'] == seat_number:
                self.reservations.remove(reservation)
                for train in self.trains:
                    if train['train_number'] == train_number:
                        train['booked_seats'].remove(seat_number)
                        print("Ticket cancelled successfully.")
                        return
        print("Reservation not found.")

    def view_booked_tickets(self, username):
        user_reservations = [res for res in self.reservations if res['username'] == username]
        if user_reservations:
            for res in user_reservations:
                print(f"Passenger Name: {res['passenger_name']}, Age: {res['passenger_age']}, Train: {res['train_number']}, From: {res['from_place']}, To: {res['to_place']}, Departure: {res['departure_time']} on {res['departure_date']}, Seat: {res['seat_number']}")
        else:
            print("No reservations found.")

    def view_train_schedule(self):
        for train in self.trains:
            print(f"Train Number: {train['train_number']}, Origin: {train['origin']}, Destination: {train['destination']}, Departure: {train['departure']}, Available Seats: {train['seats'] - len(train['booked_seats'])}")

def main():
    system = RailwaySystem()
    while True:
        print("\n1. Register\n2. Login\n3. Book Ticket\n4. Cancel Ticket\n5. View Booked Tickets\n6. View Train Schedule\n7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            system.register_user(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            system.login_user(username, password)
        elif choice == '3':
            username = input("Enter username: ")
            passenger_name = input("Enter passenger name: ")
            passenger_age = int(input("Enter passenger age: "))
            train_number = input("Enter train number: ")
            from_place = input("Enter from place: ")
            to_place = input("Enter to place: ")
            departure_time = input("Enter departure time (e.g., 09:00 AM): ")
            departure_date = input("Enter departure date (e.g., 2023-07-24): ")
            seat_number = int(input("Enter seat number: "))
            system.book_ticket(username, train_number, passenger_name, passenger_age, from_place, to_place, departure_time, departure_date, seat_number)
        elif choice == '4':
            username = input("Enter username: ")
            train_number = input("Enter train number: ")
            seat_number = int(input("Enter seat number: "))
            system.cancel_ticket(username, train_number, seat_number)
        elif choice == '5':
            username = input("Enter username: ")
            system.view_booked_tickets(username)
        elif choice == '6':
            system.view_train_schedule()
        elif choice == '7':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
