'''
------------------------------------------------Bank account balance------------------------------------------------
Problem Statement : Write a python program to calculate the remaining balance after withdrawal.
------------------------------------------------------
sample input :
Enter the current balance = 6570000.00
Enter the Withdrawal = 7695.00
------------------------------------------------------
Sample output :
Remaining Balance = 6562305.0
------------------------------------Coding----------------------------------------
'''
Current_balance = float(input("Enter the current balance: "))
Withdrawal_Amount = float(input("Enter the Withdrawal: "))
#------------Validating the inputs----------------
if Current_balance < 0 or Withdrawal_Amount < 0:
    exit("Enter valid values.")
#-------------------------------------------------
print("-------------------------------------------------------")
print("Remaining Balance",Current_balance-Withdrawal_Amount)
print("-------------------------------------------------------")