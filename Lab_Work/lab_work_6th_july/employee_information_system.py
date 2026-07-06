'''
---------------------------------------------Employee Information System----------------------------------------- 
Problem Statement: 
Create a dictionary where: 
• Employee ID is the key.  
• Value is another dictionary containing:  
o Name  
o Department  
o Salary  
Perform the following operations: 
• Display all employee details.  
• Search for an employee using Employee ID.  
• Increase the salary of all employees by 10%.  
• Display employees belonging to a specific department entered by the user. 
-----------------------------------------------------------------------------------------------------------------
-----------------------------------------Coding------------------------------------------
'''

# Employee records with Employee ID as the key
employees = {
	'E101': {'Name': 'Aarav', 'Department': 'HR', 'Salary': 40000},
	'E102': {'Name': 'Meera', 'Department': 'IT', 'Salary': 55000},
	'E103': {'Name': 'Kabir', 'Department': 'Finance', 'Salary': 50000},
	'E104': {'Name': 'Isha', 'Department': 'IT', 'Salary': 60000}
}

print("-------------------------------------------------")
print("All Employee Details:")
for employee_id, details in employees.items():
	print(employee_id, ":", details)

# Search for an employee using Employee ID
search_id = input("Enter Employee ID to search: ")
print("-------------------------------------------------")
if search_id in employees:
	print("Employee Found:", search_id, ":", employees[search_id])
else:
	print("Employee not found.")

# Increase the salary of all employees by 10%
for details in employees.values():
	details['Salary'] = round(details['Salary'] * 1.10, 2)

print("-------------------------------------------------")
print("Employee Details After 10% Salary Increase:")
for employee_id, details in employees.items():
	print(employee_id, ":", details)

# Display employees belonging to a specific department
department_name = input("Enter department name to display employees: ")
print("-------------------------------------------------")
print("Employees in", department_name, "department:")
for employee_id, details in employees.items():
	if details['Department'].lower() == department_name.lower():
		print(employee_id, ":", details)

print("-------------------------------------------------")
#----------------------------------------------------------------------------------------------------------