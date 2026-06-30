'''
--------------------------------------Monthly Salary Calculation-----------------------------------
Write a python program to calculate the total monthly salary of an employee by adding the fixed salary and incentive amount.
-----------------------------------------------------
Sample Input:
Enter the basic salary:56474.567
Enter the incentive amount:65748.0
-----------------------------------------------------
Sample Output:
total monthly salary 122222.56700000001
------------------------------------------------------
-----------------------------------------Coding------------------------------------------
'''
basicsalary=float(input("Enter the basic salary:"))
Incentive=float(input("Enter the incentive amount:"))
#-------------Validating the inputs----------------
if basicsalary < 0 or Incentive < 0:
    exit("Enter valid values.")
#--------------------------------------------------
print("--------------------------------------------------------------")
print("total monthly salary",basicsalary+Incentive)
print("--------------------------------------------------------------")
#---------------------------------------------------------------------------------------------------