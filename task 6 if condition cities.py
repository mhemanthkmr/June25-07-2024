#task 6 if condition cities

india=["mumbai","banglore","chennai","delhi"]
pakistan=["lahore","karachi","islamabad"]
bangladesh=["dhaka","khulna","rangpur"]

city=input("Enter the city name:")

if(city in india):
    print(f"{city} belongs to india")
elif(city in pakistan):
    print(f"{city} belongs to pakistan")
else:
    print(f"{city} belongs bangladhesh")


city1=input("Enter the city name:")
city2=input("Enter the city name:")

if(city1 in india and city2 in  india or city1 in pakistan and city2 in pakistan or city1 in bangladesh and city2 in bangladesh):
    print("Both states belong to same country")
else:
    print("They does not belong to the same country")
    