'''
---------------------------------------Online Examination Result Analyzer---------------------------------------
Problem Statement 
A student appears in 5 subjects. 
Rules: 
• Minimum 40 marks in every subject to pass.  
• Distinction → Average ≥ 75  
• First Division→ Average ≥ 60  
• Second Division → Average ≥ 50  
• Pass  → Average ≥ 40  
• Fail if any subject score < 40  
----------------------------------------------------------
Sample Input 
Hindi : 85 
English : 78 
Mathematics : 82 
Science : 75 
Computer : 90 
----------------------------------------------------------
Sample Output 
Average Marks: 82.0 
Result: PASS 
Classification: Distinction 
----------------------------------------------------------
-----------------------------------Coding-----------------------------------
'''
from sqlalchemy import Result


hindi_marks = int(input("Hindi (Out of 100): "))
english_marks = int(input("English (Out of 100): "))
mathematics_marks = int(input("Mathematics (Out of 100): "))
science_marks = int(input("Science (Out of 100): "))
computer_marks = int(input("Computer (Out of 100): "))
#-------------Validating the inputs----------------
if (hindi_marks < 0 or hindi_marks > 100 or english_marks < 0 or english_marks > 100 or mathematics_marks < 0 or mathematics_marks > 100 or science_marks < 0 or science_marks > 100 or computer_marks < 0 or computer_marks > 100):
    exit("Enter valid marks between 0 and 100.")
#--------------------------------------------------
total_marks = hindi_marks + english_marks + mathematics_marks + science_marks + computer_marks
average_marks = total_marks / 5
print("----------------------------------------------------------")
print(f"Average Marks: {average_marks:.1f}")
if average_marks < 40 or hindi_marks<40 or english_marks<40 or mathematics_marks<40 or science_marks<40 or computer_marks<40:
    print("Result: FAIL")
else:
    print("Result: PASS")
if average_marks>= 75:
    print("Classification: Distinction")
elif average_marks>= 60:
    print("Classification: First Division")
elif average_marks>= 50:
    print("Classification: Second Division")
print("----------------------------------------------------------")
#--------------------------------------------------------------------------------------------------------------