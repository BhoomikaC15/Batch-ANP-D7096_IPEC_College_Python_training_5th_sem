'''
-------------------------------------List Analysis using Functions-------------------------------------- 
Write a Python program that defines the following functions: 
• find_max(numbers)  
• find_min(numbers)  
• find_average(numbers)  
The program should: 
• Accept a list of 10 integers from the user.  
• Call all three functions.  
• Display the maximum value, minimum value, and average of the list. 
------------------------------------------------
---------------------------------Coding-----------------------------------
'''
# defining the function to find maximum value
def find_max(numbers):
    return max(numbers)

# defining the function to find minimum value
def find_min(numbers):
    return min(numbers)

# defining the function to find average value
def find_average(numbers):
    return sum(numbers) / len(numbers)

#-----------------------main program---------------------------------
print("-----------------------------------------------------------")
numbers = []
for i in range(10):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

max_value = find_max(numbers)
min_value = find_min(numbers)
average_value = find_average(numbers)

print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
print(f"Average value: {average_value}")
print("-----------------------------------------------------------")
#------------------------------------------------------------------------------------------------