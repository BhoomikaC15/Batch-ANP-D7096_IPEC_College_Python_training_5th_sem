'''
----------------------------------------Password Strength Checker------------------------------------------ 
Write a function check_password(password) that checks whether a password is strong. 
A password is considered Strong if: 
• It contains at least 8 characters.  
• It contains at least one uppercase letter.  
• It contains at least one lowercase letter.  
• It contains at least one digit.  
The function should return: 
• "Strong Password" or  
• "Weak Password"  
The main program should accept a password from the user and display the result.
------------------------------------------------------------------------------------------------
------------------------------------Coding------------------------------------------
'''
# function to check password strength
def check_password(password):
    if len(password) < 8:
        return "Weak Password"
    if not any(char.isupper() for char in password):
        return "Weak Password"
    if not any(char.islower() for char in password):
        return "Weak Password"
    if not any(char.isdigit() for char in password):
        return "Weak Password"
    return "Strong Password"

#-----------------------main program---------------------------------
print("-----------------------------------------------------------")
password = input("Enter a password: ")
print("Password Strength: ", check_password(password))
print("-----------------------------------------------------------")
#------------------------------------------------------------------------------------------------