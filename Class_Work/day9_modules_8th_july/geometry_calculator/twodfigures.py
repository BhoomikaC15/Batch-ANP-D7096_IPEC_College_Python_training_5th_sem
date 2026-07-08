'''
-------------------------------------Geometry Calculator Using Python Module--------------------------------------
Develop a menu-driven Python application that demonstrates the use of User-Defined Modules and Functions.
------------------------------------------------------------------------------------------------------------------
-----------------------------------Coding-----------------------------------
'''

#-----------------------------------Module for Two-Dimensional Figures-----------------------------------

# Triangle
# Function to calculate area of triangle
def triangle_area(base, height):
    return 0.5 * base * height  

# Function to calculate perimeter of triangle
def triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3

# Circle
# Function to calculate area of circle
def circle_area(radius):
    return 3.14 * radius ** 2

# Function to calculate perimeter of circle
def circle_perimeter(radius):
    return 2 * 3.14 * radius

# Square
# Function to calculate area of square  
def square_area(side):
    return side ** 2

# Function to calculate perimeter of square
def square_perimeter(side):
    return 4 * side

# Rectangle
# Function to calculate area of rectangle
def rectangle_area(length, width):
    return length * width

# Function to calculate perimeter of rectangle
def rectangle_perimeter(length, width):
    return 2 * (length + width)

#---------------------------------------------------------------------------------------------------------------