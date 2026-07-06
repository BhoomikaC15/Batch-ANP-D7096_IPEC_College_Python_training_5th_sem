'''
-------------------------------------Student Subject Report Card------------------------------------- 
Problem Statement: 
Create a nested dictionary to store marks of students in three subjects. 
Example: 
'Priya': {'Math': 78, 'Science': 95, 'English': 82}, 
'Ankit': {'Math': 91, 'Science': 89, 'English': 94} 
} 
Write a program to: 
• Calculate the total marks of each student.  
• Calculate the average marks of each student.  
• Display the topper based on total marks.  
• Display the subject-wise highest marks along with the student's name.  
• Display students whose average is greater than or equal to 85.
----------------------------------------------------------------------------------------------------------
---------------------------------Coding------------------------------------------
'''

# Sample nested dictionary of students and subject marks
student_marks = {
	'Priya': {'Math': 78, 'Science': 95, 'English': 82},
	'Ankit': {'Math': 91, 'Science': 89, 'English': 94},
	'Rahul': {'Math': 85, 'Science': 87, 'English': 90}
}

print("----------------------------------------------------------")

total_marks = {}
average_marks = {}

for student_name, subjects in student_marks.items():
	total = sum(subjects.values())
	average = total / len(subjects)
	total_marks[student_name] = total
	average_marks[student_name] = average
	print(student_name, "-> Total Marks:", total, ", Average Marks:", f"{average:.2f}")

topper_name = max(total_marks, key=total_marks.get)
print("----------------------------------------------------------")
print("Topper Based on Total Marks:", topper_name)
print("Total Marks:", total_marks[topper_name])

print("----------------------------------------------------------")
print("Subject-wise Highest Marks:")
subjects = ['Math', 'Science', 'English']
for subject in subjects:
	highest_student = max(student_marks, key=lambda student: student_marks[student][subject])
	highest_mark = student_marks[highest_student][subject]
	print(subject, ":", highest_student, "with", highest_mark)

print("----------------------------------------------------------")
print("Students with Average >= 85:")
for student_name, average in average_marks.items():
	if average >= 85:
		print(student_name, "->", f"{average:.2f}")

print("----------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------