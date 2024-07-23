India=["Mumbai","Banglore","Chennai","Delhi"]
Pakistan=["Lahore","Karachi","Islamabad"]
Bangladesh=["Dhaka","Khulna","Rangpur"]

city=str(input("Enter the city name:"))
if city in India or city in Pakistan or city in Bangladesh:
    if city in India:
        print(f'{city} belongs to India')
    else:
        if city in Pakistan:
            print(f'{city} belongs to Pakistan')
        else:
            if city in Bangladesh:
               print(f'{city} belongs to Bangladesh')
else:
    print("Not belongs to India or Pakistan or Bangladesh")
            

