'''
----------------------------------------Compound Interest Calculator----------------------------------------
Write a Python program to calculate compound interest. The program should accept the principal amount, rate of interest, 
and time period in years from the user. It should then calculate and display the compound interest and the total amount 
after the specified time period.
------------------------------------------------------------------------------------------------
---------------------------------Coding------------------------------------------
'''
Principle = float(input("Enter principal amount(Rs): "))
# --------------Validating the principle-------------
if Principle<0:
    exit("Principle cannot be zero")
#----------------------------------------------------
Rate = float(input("Enter rate of interest(%): "))
# ----------------Validating the Rate of Interest---------------
if Rate<0:
    exit("Rate of interest cannot be zero")
#---------------------------------------------------------------
Time = float(input("Enter time (years): "))
# -----------Validating the Time------------
if Time<0:
    exit("Time cannot be zero")
#-------------------------------------------

Amount = Principle * (1 + Rate / 100) ** Time
print("-----------------------------------------")
print("Amount =",Amount)
print("Compound Interest =", Amount - Principle)
print("-----------------------------------------")
#------------------------------------------------------------------------------------------------