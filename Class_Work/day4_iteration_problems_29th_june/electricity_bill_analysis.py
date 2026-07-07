'''
-------------------------------------------------Electricity Bill Analgitysis----------------------------------------
Problem Statement
An electricity department wants to analyze electricity consumption of N houses.
Accept the monthly units consumed by each house.
Calculate and display:
• Total units consumed
• Average units consumed
• Highest consumption
• Lowest consumption
----------------------------------------------------------------
Sample Output
Enter the number of houses: 4
Enter units consumed by house 1: 150
Enter units consumed by house 2: 200
Enter units consumed by house 3: 120
Enter units consumed by house 4: 180
-------------------------------------------------
Total units consumed: 650
Average units consumed: 162.5
Highest consumption: 200
Lowest consumption: 120
-------------------------------------------------
------------------------------------------Coding----------------------------------------
'''
# Input number of houses
n = int(input("Enter the number of houses: "))
print("-------------------------------------------------")

# Initialize variables
units_list = []
total_units = 0

# Input units for each house
for i in range(1, n + 1):
    units = int(input(f"Enter units consumed by house {i}: "))
    units_list.append(units)
    total_units = total_units + units

print("-------------------------------------------------")

# Calculate average
average_units = total_units / n

# Find highest and lowest consumption
highest_consumption = max(units_list)
lowest_consumption = min(units_list)

# Display results
print("Total units consumed:", total_units)
print("Average units consumed:", average_units)
print("Highest consumption:", highest_consumption)
print("Lowest consumption:", lowest_consumption)
print("-------------------------------------------------")
#----------------------------------------------------------------------------------------------------------