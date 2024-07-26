
# num = int(input("enter the value: "))

# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()    



base = float(input("Enter the base value: "))
height = float(input("Enter the base value: "))
shape = input("enter the shape: ")

if (shape == "triangle"):
    area = (1/2)*base*height
    print("Area of triangle is: ",area)
elif(shape =="rectangle"):
    area = base*height
    print("Area of rectangle is:", area)
else:
    print("Invalid shape") 
    

