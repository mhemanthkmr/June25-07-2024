# function to calculate area
def calculate_triangle_area():

    base=int(input("Enter the value of base: "))
    height=int(input("Enter the value of height: "))
    area=(1/2*base*height)
    return area

def print_triangle_area():
    area=calculate_triangle_area()
    print(f"The area of the triangle is:{area}")

#calculate shapetype:
def calculate(length,width,shapeType):
    if(shapeType=="triangle"):
        area=(1/2)*length*width
    
    elif(shapeType=="rectangle"):
        area= length*width
        return area
    else:
        print("invalid")

length=float(input("enter length:"))
width=float(input("enter width:"))
triangle_area=calculate(length,width,"triangle")
rectangle_area=calculate(length,width,"rectangle")
print(triangle_area)
print(rectangle_area)

