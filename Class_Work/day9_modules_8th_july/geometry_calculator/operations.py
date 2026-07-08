#---------------------------------main program for Geometry Calculator---------------------------------
# importing the module for two-dimensional figures
from twodfigures import *
#----------------------------------------------------------

while True:
    print("\nGeometry Calculator Menu:")
    print("1. Square")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Circle")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    # Calling the functions based on user choice for Square
    if choice == '1':
        side = float(input("Enter the side length of the square: "))
        print("1. Area")
        print("2. Perimeter")
        option = input("Enter '1' to calculate area or '2' to calculate perimeter: ")
        if option == '1':
            print("Area of square:", square_area(side))
        elif option == '2':
            print("Perimeter of square:", square_perimeter(side))
        else:
            print("Invalid option. Please try again.")

    # Calling the functions based on user choice for Rectangle
    elif choice == '2':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print("1. Area")
        print("2. Perimeter")
        option = input("Enter '1' to calculate area or '2' to calculate perimeter: ")
        if option == '1':
            print("Area of rectangle:", rectangle_area(length, width))
        elif option == '2':
            print("Perimeter of rectangle:", rectangle_perimeter(length, width))
        else:
            print("Invalid option. Please try again.")

    # Calling the functions based on user choice for Triangle
    elif choice == '3':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        side1 = float(input("Enter the length of side 1 of the triangle: "))
        side2 = float(input("Enter the length of side 2 of the triangle: "))    
        side3 = float(input("Enter the length of side 3 of the triangle: "))
        print("1. Area")
        print("2. Perimeter")
        option = input("Enter '1' to calculate area or '2' to calculate perimeter: ")
        if option == '1':
            print("Area of triangle:", triangle_area(base, height))
        elif option == '2':
            print("Perimeter of triangle:", triangle_perimeter(side1, side2, side3))
        else:
            print("Invalid option. Please try again.")

    # Calling the functions based on user choice for Circle
    elif choice == '4':
        radius = float(input("Enter the radius of the circle: "))
        print("1. Area")
        print("2. Perimeter")
        option = input("Enter '1' to calculate area or '2' to calculate perimeter: ")
        if option == '1':
            print("Area of circle:", circle_area(radius))
        elif option == '2':
            print("Perimeter of circle:", circle_perimeter(radius))
        else:
            print("Invalid option. Please try again.")

    elif choice == '5':
        print("Exiting the Geometry Calculator.")
        break

    else:
        print("Invalid choice. Please try again.")

#-------------------------------------------------------------------------------------------------