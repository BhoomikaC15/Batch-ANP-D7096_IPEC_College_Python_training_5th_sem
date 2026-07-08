#-----------------------importing the module using import keyword----------------------------
# importing the module
import numeric_calculator
#----------------------------------------------------------
a = 6
b = 12

print("----------------------------------------------")
# calling the add function from the module
print("Sum is: ", numeric_calculator.add(a, b))

# calling the subtract function from the module
print("Difference is: ", (numeric_calculator.subtract(a, b)))

# calling the multiply function from the module
print("Product is: ", numeric_calculator.multiply(a, b))
    
# calling the divide function from the module
print("Quotient is: ", numeric_calculator.divide(a, b))

# calling the remainder function from the module
print("Remainder is: ", numeric_calculator.remainder(a, b))
print("----------------------------------------------")
#--------------------------------------------------------------------------------------------------