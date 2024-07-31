def area(base,height,shape):
    if(shape=="triangle"):
        area=0.5*base*height
        return area
    elif(shape=="rectangle"):
        area=base*height
        return area
    else:
        print("invalid shape")

base=float(input("ENter the firrst measurement:"))
height=float(input("ENter the second parameter:"))
shape=input("Enter the shape:").strip().lower()
ans=area(base,height,shape)
print(ans)