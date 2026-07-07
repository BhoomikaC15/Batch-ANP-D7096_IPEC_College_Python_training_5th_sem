'''
-------------------------------------------------Employee Salary Statistics----------------------------------------
Problem Statement
A company has N employees.
Accept the salary of each employee and determine:
• Highest salary
• Lowest salary
• Average salary
• Number of employees earning more than ₹50,000
----------------------------------------------------------------
Sample Output
Enter the number of employees: 5
Enter salary of employee 1: 45000
Enter salary of employee 2: 65000
Enter salary of employee 3: 55000
Enter salary of employee 4: 75000
Enter salary of employee 5: 50000
-------------------------------------------------
Highest salary: 75000
Lowest salary: 45000
Average salary: 58000.0
Employees earning more than 50000: 3
-------------------------------------------------
------------------------------------------Coding----------------------------------------
'''
# Input number of employees
n = int(input("Enter the number of employees: "))
print("-------------------------------------------------")

# Initialize variables
salary_list = []
total_salary = 0
count_above_50000 = 0

# Input salary for each employee
for i in range(1, n + 1):
    salary = int(input(f"Enter salary of employee {i}: "))
    salary_list.append(salary)
    total_salary = total_salary + salary
    
    # Count employees earning more than 50000
    if salary > 50000:
        count_above_50000 = count_above_50000 + 1

print("-------------------------------------------------")

# Calculate statistics
highest_salary = max(salary_list)
lowest_salary = min(salary_list)
average_salary = total_salary / n

# Display results
print("Highest salary:", highest_salary)
print("Lowest salary:", lowest_salary)
print("Average salary:", average_salary)
print("Employees earning more than 50000:", count_above_50000)
print("-------------------------------------------------")
#----------------------------------------------------------------------------------------------------------