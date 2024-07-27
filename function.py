"""function
1. returnable
2. non returnable"""
# find the given number is odd or even
def even_odd(number):
    if number%2==0:
        return True
    else:
        return False
result=even_odd(8)
print(result)


# """ Arbitary Arguments
# n number of args are passed inside the function parameters"""
def functname(*arg):
    for i in arg:
        print(functname(i[0],i[1]))


# #sum 2 numbers
def sum(a,b=0):
    return a+b
print(sum(5,10))


# # area of triangle
def area_of_triangle(base,height):
    return int((1/2)*base*height)
print(area_of_triangle(5,10))


# #area of rectangle/square
def area_of_shape(base,height,shape_type):
    if shape_type=="triangle":
        return int((1/2)*base*height)
    elif shape_type=="rectangle":
        return base*height
    else:
        return "unsupported shape"
print(area_of_shape(5,10,"triangle"))
print(area_of_shape(5,10,"rectangle"))

#pattern match
def pattern(n):
    for i in range(1,n+1):
        # for j in range(1,i+1):
        #     print("*",end=" ")
        # print()
n=6
pattern(n)
