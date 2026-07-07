'''
--------------------------------------Grocery bill calculator--------------------------------------
Problem Statement: 
write a python program to calculate the total cost of rice packets purchased.
---------------------------------Coding--------------------------------------
'''
Price=float(input("enter the price per rice packet "))
Number_of_packet =int(input("enter the number of rice "))
#-------------Validating the inputs----------------
if Price < 0 or Number_of_packet < 0:
    exit("Enter valid values.")
#--------------------------------------------------
Total_cost=Price*Number_of_packet
print("--------------------------------------")
print("Total Cost: ",Total_cost)
print("--------------------------------------")
#------------------------------------------------------------------------------------------------