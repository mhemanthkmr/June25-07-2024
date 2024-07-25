rooms={101:True,102:True,103:True,104:True,105:True}
bookings=[]
while True:
    print("""
          Hotel Booking System
             1. List available rooms
             2. Book a room
             3. Check out
             4. Exit
         """)
    choice=int(input("Enter your choices:"))
    if(choice==1):
        print(f"list of available rooms{rooms}")
    elif(choice==2):
        roomnumber=int(input("Enter the room number:"))
        if roomnumber in rooms and rooms[roomnumber]:
           guestname=input("Enter guest name:")
           guestage=int(input("Enter guest age:"))
           rooms[roomnumber] = False
           bookings.append((roomnumber, guestname, guestage))
           print(f"Room {roomnumber} successfully booked for {guestname}.")
        else:
          print("please enter available rooms:")
    elif(choice==3):
        roomnumber=int(input("Enter room number to check out:")) 
    elif(choice==4):
        print("program successfully executed")
        break
    else:
        print(" Please try again.")