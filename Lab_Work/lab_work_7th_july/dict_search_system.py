'''
--------------------------------------------Dictionary Search System------------------------------------------ 
Write a Python program that defines a function search_student(student_dict, roll_no). 
The function should: 
• Accept a dictionary where:  
o Key = Roll Number  
o Value = Student Name  
• Search for the given roll number.  
• Return the student name if found; otherwise return "Student Not Found".  
The main program should: 
• Create a dictionary of at least 5 students.  
• Accept a roll number from the user.  
• Display the search result. 
------------------------------------------------
---------------------------------Coding-----------------------------------
'''
# defining the function to search student
def search_student(student_dict, roll_no):
    return student_dict.get(roll_no, "Student Not Found")

#-----------------------main program---------------------------------
print("-----------------------------------------------------------")
student_dict = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David",
    105: "Eve"
}
roll_no = int(input("Enter the roll number to search: "))
print("Search Result: ", search_student(student_dict, roll_no))
print("-----------------------------------------------------------")
#------------------------------------------------------------------------------------------------