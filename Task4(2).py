#task4
#list of cities per country

india=["mumbai","bangalore","chennai","delhi"]
pakistan=["lahore","karachi","islamabad"]
bangladesh=["dhaka","khulna","rangpur"]
print(india)
print(pakistan)
print(bangladesh)

#a=str(input("Enter your city name:"))
#b=str(input("Enter your country name:"))

#print(a,b)

x=input("Enter your city name:")
y=input("Enter your city name:")

if x in india :
    if y in india:
     print("both cities in india")
else:
    print("not in india")

