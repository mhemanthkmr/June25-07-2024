#task 4
#list of cities:

india=["mumbai","banglore","chennai","delhi"]
pakistan=["lahore","karachi","islamabad"]
bangladesh=["dhaka","khulna","rangpur"]
print(india)
print(pakistan)
print(bangladesh)

record1=str(input("Enter the city name:"))
record2=str(input("Enter the city that belongs to: "))
print(record1 ) 
print(record2)

#if condition:

city1=input("Enter the city name:")
city2=input("Enter the city name:")
if city1 in india and city2 in india:
    print("Both in india")
else:
    print("Not in india")

#sugar level identifi:

sugar=int(input("Enter the sugar level:"))
if sugar>=100:
    print("high")
elif sugar<80:
    print("low")
else:
    print("normal")
    
