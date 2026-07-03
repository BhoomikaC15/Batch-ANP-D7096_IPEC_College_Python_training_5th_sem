'''
----------------------------------------Display Odd Numbers----------------------------------------
Write a program to to create a tuple of 15 numbers and display all the odd numbers from the tuple.
------------------------------------------------------------------------------------------------
Sample Input
Enter numbers:
Enter a number: 2
Enter a number: 4
Enter a number: 5
-------------------------------------
Sample Output
Odd Numbers in the tuple are:
5
------------------------------------------------------------------------------------------------
---------------------------------------Coding------------------------------------------
'''
#Creating a tuple of 15 numbers
L=[]
for i in range(15):
    num=int(input("Enter a number: "))
    L.append(num)
T=tuple(L)
print("-------------------------------------------------")
print("Odd Numbers in the tuple are:")
for i in T:
    if i%2!=0:
        print(i, sep=", ")
print("-------------------------------------------------")
#-----------------------------------------------------------------------------------------------------------