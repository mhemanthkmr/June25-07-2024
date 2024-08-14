def areaoftriangle(base,height):
    area=(1/2*height*base)
    return area


base=int(input("enter the base:"))
height=int(input("enter the height:"))
area = areaoftriangle(base,height)
print(f"area of triangle :{area}")

