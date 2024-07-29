#def returnablefunction(a,b):
#     return a+b;
# print(returnablefunction(5,7))

# def area_of_triangle(base,height):
#     return 1/2 * base* height;
# print(area_of_triangle (5,10))


def calculate_area(base,height,shape_type):
    if shape_type == "triangle":
        return int((1/2) * base* height)
    elif shape_type == "rectangle":
        return height*base
    else :
        return "invalid shape"
print(calculate_area (24,10,"triangle"))
print(calculate_area (51,10,"rectangle"))


# Print pattern
# def print_pattern(n):
#     for i in range(1, n + 1):
#         print('*' * i)
# print_pattern(5)
  