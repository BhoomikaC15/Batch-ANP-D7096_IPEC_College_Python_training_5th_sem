#-----------------------------------Module for Numeric Calculator-----------------------------------
# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b

# Function to find remainder of two numbers
def remainder(a, b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a % b

#-----------------------------------------------------------------------------------------------------