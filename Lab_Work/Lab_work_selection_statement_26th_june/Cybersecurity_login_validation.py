'''
---------------------------------------------Cybersecurity Login Validation---------------------------------------------
Problem Statement 
A login system validates: 
• Username  
• Password  
• OTP  
Conditions: 
• All correct → Login Successful  
• Incorrect OTP → Re-enter OTP  
• Incorrect Password after 3 attempts → Account Locked  
• Incorrect Username → User Not Found  
----------------------------------------------------------------
Sample Input 
Username: admin 
Password: admin123 
OTP: 4567 
----------------------------------------------------------------
Sample Output 
Login Successful 
Welcome Admin 
----------------------------------------------------------------
--------------------------------------------Coding--------------------------------  
'''

# Correct credentials (reference)
correct_username = 'admin'
correct_password = 'admin123'
correct_otp = '4567'

print("-------------------------------------------------")
username = input("Username: ")
print("-------------------------------------------------")

if username != correct_username:
	print("User Not Found")
else:
	# Password validation with up to 3 attempts
	attempts = 0
	authenticated = False
	while attempts < 3:
		password = input("Password: ")
		if password == correct_password:
			authenticated = True
			break
		else:
			attempts += 1
			if attempts < 3:
				print(f"Incorrect Password. Attempts left: {3 - attempts}")
	if not authenticated:
		print("Account Locked")
	else:
		print("-------------------------------------------------")
		# OTP validation - allow re-entry until correct
		while True:
			otp = input("OTP: ")
			if otp == correct_otp:
				print("Login Successful")
				print("Welcome", username.capitalize())
				break
			else:
				print("Incorrect OTP. Please re-enter OTP.")

print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------