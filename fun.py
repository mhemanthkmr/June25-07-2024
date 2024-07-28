# The area of the triangle
"""def calculate_area(base, height):
    area = 0.5 * base * height
    return area
base = 10
height = 5
triangle_area = calculate_area(base, height)
print(f"The area of the triangle is: {triangle_area}")"""

#Calculate the area of a shape (triangle or rectangle).
"""
def calculate_area(base, height, shape_type="triangle"):
    
    if shape_type == "triangle":
        area = 0.5 * base * height
    elif shape_type == "rectangle":
        area = base * height
    else:
        raise ValueError("Invalid shape_type.")
    return area

base = 10
height = 5

default_area = calculate_area(base, height)
print(f"The area of the default shape (triangle) is: {default_area}")

triangle_area = calculate_area(base, height, "triangle")
print(f"The area of the triangle is: {triangle_area}")

rectangle_area = calculate_area(base, height, "rectangle")
print(f"The area of the rectangle is: {rectangle_area}")"""

# print pattern
def print_pattern(n):
   
    for i in range(1, n + 1):
        print('*' * i)
print_pattern(3)
print()
print_pattern(4)




