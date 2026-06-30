'''
-------------------------------------Mobile Recharge Plan-----------------------------------
Scenario:
A telecom company charges a fixed amount per GB of data.
Problem Statement:
Write a Python program to calculate the total recharge amount based on the data pack selected.
Input:
• Cost per GB
• Number of GBs
Output:
• Total Recharge Cost
--------------------------------------------------------------
Sample Input:
Enter Cost per GB: 10
Enter Number of GBs: 5
--------------------------------------------------------------
Sample Output:
Total Recharge Cost: 50.0
--------------------------------------------------------------
--------------------------------------Coding----------------------------------------
'''
cost_per_gb = float(input("Enter Cost per GB: "))
number_of_gbs = float(input("Enter Number of GBs: "))
#-------------Validating the inputs----------------
if cost_per_gb < 0 or number_of_gbs < 0:
    exit("Enter valid values.")
#--------------------------------------------------
print("--------------------------------------------------------------")
total_recharge_cost = cost_per_gb * number_of_gbs
print("Total Recharge Cost:", total_recharge_cost)
print("--------------------------------------------------------------")
#---------------------------------------------------------------------------------------------------