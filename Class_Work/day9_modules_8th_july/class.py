# Defining a class to perform operations on rectangle
class Rectangle:
    # member variables
    length = 0
    breadth = 0

    # method to initialize the data
    def initialize(self, l, b):
        self.length = l
        self.breadth = b

    # method to display data
    def display_data(self):
        print("--------------------------------------------")
        print("Length: ", self.length, "cm")
        print("Breadth: ", self.breadth, "cm")
        print("--------------------------------------------")
#------------------------------------------------------------------

#-------------------------main program-------------------------------
# creating an object of the class
rect = Rectangle()
rect.initialize(10, 5)
rect.display_data()
#----------------------------------------------------------------------------------------------------------