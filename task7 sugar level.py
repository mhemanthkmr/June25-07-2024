#task 7 sugar level

sugar_level=int(input("Enter the fasting sugar level:"))

if(sugar_level<80):
    print("your sugar level is low")
elif(sugar_level>100):
    print("your sugar level is high")
else:
    print("your sugar level is normal")