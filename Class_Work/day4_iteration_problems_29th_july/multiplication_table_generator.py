'''
-------------------------------------------------Multiplication Table Generator----------------------------------------
Problem Statement
Generate a multiplication table for a given number.
----------------------------------------------------------------
Sample Output
Enter a number: 5
Multiplication Table for 5:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
----------------------------------------------------------------
------------------------------------------Coding----------------------------------------
'''
number = int(input("Enter a number: "))
print(f"Multiplication Table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
#----------------------------------------------------------------------------------------------------------