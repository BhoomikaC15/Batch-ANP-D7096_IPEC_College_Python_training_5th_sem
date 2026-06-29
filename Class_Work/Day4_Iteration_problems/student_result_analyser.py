'''
-------------------------------------------------Student Result Analyzer----------------------------------------
Problem Statement
A teacher wants to analyze the marks of N students.
Accept the marks of each student (out of 100).
Finally display:
• Highest Marks
• Lowest Marks
• Average Marks
• Number of students who passed (Marks ≥ 40)
• Number of students who scored distinction (Marks ≥ 75)
----------------------------------------------------------------
Sample Output
Enter the number of students: 5
Enter marks of student 1: 85
Enter marks of student 2: 35
Enter marks of student 3: 78
Enter marks of student 4: 45
Enter marks of student 5: 92
-------------------------------------------------
Highest Marks: 92
Lowest Marks: 35
Average Marks: 67.0
Students Passed: 4
Students with Distinction: 3
-------------------------------------------------
------------------------------------------Coding----------------------------------------
'''
# Input number of students
n = int(input("Enter the number of students: "))
print("-------------------------------------------------")

# Initialize variables
marks_list = []
total_marks = 0
passed_count = 0
distinction_count = 0

# Input marks for each student
for i in range(1, n + 1):
    marks = int(input(f"Enter marks of student {i}: "))
    marks_list.append(marks)
    total_marks = total_marks + marks
    
    # Count students who passed (marks >= 40)
    if marks >= 40:
        passed_count = passed_count + 1
    
    # Count students with distinction (marks >= 75)
    if marks >= 75:
        distinction_count = distinction_count + 1

print("-------------------------------------------------")

# Calculate statistics
highest_marks = max(marks_list)
lowest_marks = min(marks_list)
average_marks = total_marks / n

# Display results
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Average Marks:", average_marks)
print("Students Passed:", passed_count)
print("Students with Distinction:", distinction_count)
print("-------------------------------------------------")
#----------------------------------------------------------------------------------------------------------