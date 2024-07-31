

def custinfo():
    print("Name :",name)
    print("Mobile No :",mobile)

def local():
    print("Rupees 20 for less then 40 kilometers")
    print("Pickup Location :",pickup)
    print("Drop Location :",drop)
    print("Distance :",km)
    rupee=20
    expence=rupee*km
    print("expence :",expence)
    print(f""" Your Taxi booked successfully
          our driver contact on {date}""")
def long():
    print("Rupees 30 for more then 40 kilometers")
    print("Pickup Location :",pickup)
    print("Drop Location :",drop)
    print("Distance :",km)
    rupee=30
    expence=rupee*km
    print("expence :",expence)
    print(f""" Your Taxi booked successfully
          our driver contact on {date}""")
def enq():
    print("""          Trip Expence
          
          Rupees 20 for less then 40 kilometers
          Rupees 30 for more then 40 kilometers
          """)
    if(km<40):
        local()
    elif(km>40):
        long()
    else:
        print("Wrong Answer")

def exit():
    print("""Thanks for your visit 
         """)


print(""" 
      
       Register your details
      """)
name=input("Name :")
mobile=int(input("Mobile No :"))
pickup=input("Pickup Location :")
drop=input("Drop Location :")
date=input("Travel Date :")
km=float(input("Distance :"))


print("""
      
        BOOK YOUR TAXI
                  ANY WHERE TO GO
      
             Press 1 to Book a trip
             Press 2 to Enquiry
             Press 3 to Exit
          """)   
while True:
    choice=input("""Press your choice :""")
    if(choice=='1'):
        if(km<40):
            print("""
                  Local Trip""")
            custinfo()
            local()
            print("""
                  Conform your booking press 3
                  """)
        elif(km>40):
            print("""
                  Long Trip""")
            custinfo()
            long()
            print("""
                  Conform your booking press 3
                  """)
    elif(choice=='2'):
        enq()
    
    elif(choice=='3'):
        exit()
        break
