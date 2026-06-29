'''
-------------------------------------------------Bank Transaction Summary----------------------------------------
Problem Statement
A customer keeps entering transaction amounts.
Positive numbers indicate deposits, while negative numbers indicate withdrawals.
The customer enters 0 to finish.
Display:
• Total Deposit
• Total Withdrawal
• Final Balance
----------------------------------------------------------------
Sample Output
Enter transaction amount (0 to finish): 5000
Enter transaction amount (0 to finish): 2000
Enter transaction amount (0 to finish): -1500
Enter transaction amount (0 to finish): -500
Enter transaction amount (0 to finish): 0
-------------------------------------------------
Total Deposit: 7000
Total Withdrawal: 2000
Final Balance: 4500
-------------------------------------------------
------------------------------------------Coding----------------------------------------
'''
# Initialize variables
total_deposit = 0
total_withdrawal = 0

# Accept transaction amounts until 0 is entered
while True:
    transaction = int(input("Enter transaction amount (0 to finish): "))
    
    if transaction == 0:
        break
    elif transaction > 0:
        # Positive number - Deposit
        total_deposit = total_deposit + transaction
    else:
        # Negative number - Withdrawal
        total_withdrawal = total_withdrawal + abs(transaction)

print("-------------------------------------------------")

# Calculate final balance
final_balance = total_deposit - total_withdrawal

# Display results
print("Total Deposit:", total_deposit)
print("Total Withdrawal:", total_withdrawal)
print("Final Balance:", final_balance)
print("-------------------------------------------------")
#----------------------------------------------------------------------------------------------------------