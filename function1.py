base = int(input('Enter the base value: '))
height = int(input('Enter the height value: '))
shapetype = input('Enter the shape type (triangle/rectangle): ')

def calculate_area(base, height, shapetype):
    if shapetype == "triangle":
        area = (1/2) * base * height
        print(f'Area of the triangle: {area}')
    elif shapetype == "rectangle":
        area = base * height
        print(f'Area of the rectangle: {area}')
    else:
        print("Shape type not found")
        return None  
        
    return area

calculate_area(base, height, shapetype)



