class Train:
    def __init__(self, train_number, origin, destination, departure_time, arrival_time, total_seats, available_seats=None):
        self.train_number = train_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.total_seats = total_seats
        self.available_seats = available_seats if available_seats is not None else total_seats
    
    def __str__(self):
        return f"Train {self.train_number}: {self.origin} to {self.destination}, Departure: {self.departure_time}, Arrival: {self.arrival_time}, Available seats: {self.available_seats}/{self.total_seats}"
    
    def book_seat(self):
        if self.available_seats > 0:
            self.available_seats -= 1
            print(f"Seat booked on Train {self.train_number}. Remaining seats: {self.available_seats}/{self.total_seats}")
            return True
        else:
            print(f"Sorry, no seats available on Train {self.train_number}.")
            return False

# Create trains
trains = [
    Train("T123", "salem", "chennai", "08:00", "10:30", 100),
    Train("T456", "madurai", "chennai", "12:00", "15:30", 120),
    Train("T789", "theni", "chennai", "09:30", "18:00", 150)
]

# Display available trains
print("Available trains:")
for train in trains:
    print(train)
print()

# Get user input for booking
while True:
    train_number = input("Enter the train number ('q'): ").strip().upper()
    
    if train_number == 'Q':
        print("Exiting booking system.")
        break
    
    found_train = None
    for train in trains:
        if train.train_number == train_number:
            found_train = train
            break
    
    if found_train:
        name = input("Enter your name: ").strip()
        age = input("Enter your age: ").strip()
        from_place = input("Enter your departure place: ").strip()
        to_place = input("Enter your destination place: ").strip()
        time = input("Enter your preferred departure time: ").strip()
        date = input("Enter your preferred departure date: ").strip()
        
        if found_train.book_seat():
            print("Booking successful.")
            print(f"Booking Details:")
            print(f"Train: {found_train.train_number}")
            print(f"Name: {name}")
            print(f"Age: {age}")
            print(f"From: {from_place}")
            print(f"To: {to_place}")
            print(f"Departure Time: {time}")
            print(f"Departure Date: {date}")
            print("Enjoy your journey!")
            print()
        else:
            print("Booking failed. No seats available.")
            print()
    else:
        print(f"Train with number {train_number} not found.")
        print()


