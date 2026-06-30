'''
-------------------------------------Problem statement :fuel consumption tracker-----------------------------------
Write a python program to find the average mileage of car.
-------------------------------------------------------
Sample input :
Enter the Total distance (km): 456
Enter the Fuel consumed(liters): 6
-------------------------------------------------------
Sample output :
Mileage(km/l): 6.8059701    
-------------------------------------------------------
------------------------------------Coding----------------------------------------
'''
Total_Distance= float(input("Enter the Total distance (km): "))
Fuel_Consumed= float(input("Enter the Fuel consumed(liters): "))
#-------------Validating the inputs----------------
if Total_Distance < 0 or Fuel_Consumed <= 0:
    exit("Enter valid values.")
#--------------------------------------------------
print("--------------------------------------------------------------")
print("Mileage(km/l):", round(Total_Distance/Fuel_Consumed, 6))
print("--------------------------------------------------------------")
#---------------------------------------------------------------------------------------------------