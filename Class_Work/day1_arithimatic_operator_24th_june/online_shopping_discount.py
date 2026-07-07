'''
----------------------------------------------Online Shopping Discount-------------------------------------------
Scenario:
An e-commerce website offers a fixed discount on products.
Problem Statement:
Write a Python program to calculate the final payable amount after applying the discount.
Input:
• Product Price
• Discount Amount
Output:
• Final Price
--------------------------------------------------------------
Sample Input:
Enter Product Price: 1000
Enter Discount Amount: 200
--------------------------------------------------------------
Sample Output:
Final Price: 800.0
--------------------------------------------------------------
--------------------------------------Coding----------------------------------------
'''
product_price = float(input("Enter Product Price: "))
discount_amount = float(input("Enter Discount Amount: "))
#-------------Validating the inputs----------------
if product_price < 0 or discount_amount < 0:
    exit("Enter valid values.")
#--------------------------------------------------
final_price = product_price - discount_amount
print("--------------------------------------------------------------")
print("Final Price:", final_price)
print("--------------------------------------------------------------")
#---------------------------------------------------------------------------------------------------