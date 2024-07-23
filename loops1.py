india = ["mumbai", "bangalore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city1=input("Enter the city name:")
city2=input("Enter the city name:")

if(city1 in india)and(city2 in india):
    print("Both the cities are in india")
else:
    if(city1 in pakistan)and(city2 in pakistan):
        print("Both the cities are in pakistan")
    else:
        if(city1 in bangladesh)and(city2 in bangladesh):
            print("Both the cities are in bangladesh")
        else:
            print("Both the cities are not in the country")

