India=["Mumbai","Banglore","Chennai","Delhi"]
Pakistan=["Lahore","Karachi","Islamabad"]
Bangladesh=["Dhaka","Khulna","Rangpur"]

city1=str(input("Enter the city name:"))
city2=str(input("Enter the city name:"))
if (city1 in India) and (city2 in India):
    print(f'{city1} and {city2} they both or in India')
else:
    if (city1 in Pakistan) and (city2 in Pakistan):
        print(f'{city1} and {city2} they both or in Pakistan')
    else:
        if (city1 in Bangladesh) and  (city2 in Bangladesh):
            print(f'{city1} and {city2} they both or in Bangladesh')
        else:
            print("they are not in same city")
               
