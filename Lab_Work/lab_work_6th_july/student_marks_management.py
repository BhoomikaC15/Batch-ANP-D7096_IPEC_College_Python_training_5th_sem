'''
-----------------------------------------Student Marks Management---------------------------------------
Problem Statement: 
Create a dictionary to store the marks of 5 students, where the key is the student's name and the 
value is their marks. 
Perform the following operations: 
• Display all student names and marks.  
• Add a new student with marks.  
• Update the marks of an existing student.  
• Delete a student by name.  
• Display the student who scored the highest marks.  
---------------------------------------------------------------------------------------------------------
'''
#-------------------------------------------Coding-----------------------------------------

# Create a dictionary to store marks of 5 students
student_marks = {}

for i in range(1, 6):
	student_name = input(f"Enter student {i} name: ")
	marks = int(input(f"Enter marks for {student_name}: "))
	student_marks[student_name] = marks

print("-------------------------------------------------")
print("All Student Names and Marks:")
for student_name, marks in student_marks.items():
	print(student_name, ":", marks)

# Add a new student with marks
new_student_name = input("Enter new student name to add: ")
new_student_marks = int(input(f"Enter marks for {new_student_name}: "))
student_marks[new_student_name] = new_student_marks

# Update the marks of an existing student
update_student_name = input("Enter student name to update: ")
if update_student_name in student_marks:
	updated_marks = int(input(f"Enter new marks for {update_student_name}: "))
	student_marks[update_student_name] = updated_marks
else:
	print("Student not found for update.")

# Delete a student by name
delete_student_name = input("Enter student name to delete: ")
if delete_student_name in student_marks:
	del student_marks[delete_student_name]
else:
	print("Student not found for deletion.")

print("-------------------------------------------------")
print("Updated Student Marks:")
for student_name, marks in student_marks.items():
	print(student_name, ":", marks)

# Display the student who scored the highest marks
if student_marks:
	topper_name = max(student_marks, key=student_marks.get)
	topper_marks = student_marks[topper_name]
	print("-------------------------------------------------")
	print("Highest Marks Student:", topper_name)
	print("Marks:", topper_marks)
	print("-------------------------------------------------")
else:
	print("No student records available.")

#----------------------------------------------------------------------------------------------------------
