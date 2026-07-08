#----------------------------importing module with specific function name-----------------------------
# importing the module
from numeric_calculator import add, subtract, multiply, divide, remainder
#----------------------------------------------------------
a = 12
b = -6

print("----------------------------------------------")
# calling the add function from the module
print("Sum is: ", add(a, b))

# calling the subtract function from the module
print("Difference is: ", subtract(a, b))

# calling the multiply function from the module
print("Product is: ", multiply(a, b))

# calling the divide function from the module
print("Quotient is: ", divide(a, b))

# calling the remainder function from the module
print("Remainder is: ", remainder(a, b))
print("----------------------------------------------")
#--------------------------------------------------------------------------------------------------