'''
-------------------------------------------------Login System with Maximum Attempts----------------------------------------
Problem Statement
A system allows only three login attempts.
The correct username is admin and the password is python123.
If the credentials are correct, display "Login Successful".
Otherwise, after three unsuccessful attempts, display "Account Locked".
----------------------------------------------------------------
Sample Output
Attempt 1
Username: admin
Password: abc

Invalid Credentials

Attempt 2
Username: admin
Password: python123

Login Successful
----------------------------------------------------------------
------------------------------------------Coding----------------------------------------
'''
# Define correct credentials
correct_username = "admin"
correct_password = "python123"
max_attempts = 3

# Loop for login attempts
for attempt in range(1, max_attempts + 1):
    print(f"Attempt {attempt}")
    username = input("Username: ")
    password = input("Password: ")
    print()
    
    # Check if credentials are correct
    if username == correct_username and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
        print()
else:
    # This else block executes if the loop completes without break
    print("Account Locked")

print("-------------------------------------------------")
#----------------------------------------------------------------------------------------------------------