#function to calculate area:

def calculateArea(base,height):
    area=(1/2)*base*height
    return area

base=int(input("Enter your firstValue:"))
height=int(input("Enter your secondValue:"))
print(calculateArea(base,height))
base=12
height=34
area=calculateArea(base,height)
print(area)

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
