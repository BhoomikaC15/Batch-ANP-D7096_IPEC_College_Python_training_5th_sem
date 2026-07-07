'''
----------------------------------Simple Interest----------------------------------
Write a Python function to calculate simple interest. The function should take three parameters: principal amount, rate of interest, and time period in years. It should return the calculated simple interest.
-----------------------------------------------------------------------------------
-----------------------------------Coding---------------------------------
'''
# function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    return ((principal * rate * time) / 100)
#--------------------------------------------------------
# main program
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = int(input("Enter the time period in years: "))
print("-------------------------------------------------")
print("The simple interest is:", calculate_simple_interest(principal, rate, time))
print("-------------------------------------------------")
#---------------------------------------------------------------------------------------------