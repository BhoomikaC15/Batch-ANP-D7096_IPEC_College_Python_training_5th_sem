#--------------------------------------importing the module using alias--------------------------------------
# importing the module
import numeric_calculator as nc
#----------------------------------------------------------
a = 6
b = -12

print("----------------------------------------------")
# calling the add function from the module
print("Sum is: ", nc.add(a, b))

# calling the subtract function from the module
print("Difference is: ", (nc.subtract(a, b)))

# calling the multiply function from the module
print("Product is: ", nc.multiply(a, b))

# calling the divide function from the module
print("Quotient is: ", nc.divide(a, b))

# calling the remainder function from the module
print("Remainder is: ", nc.remainder(a, b))
print("----------------------------------------------")
#--------------------------------------------------------------------------------------------------