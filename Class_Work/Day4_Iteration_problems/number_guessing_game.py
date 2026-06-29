'''
----------------------------------------Number Guessing Game---------------------------------------
Problem Statement 
A secret number is 37. 
Keep asking the user to guess the number until the correct number is entered. 
Display whether the entered number is too high, too low, or correct.
----------------------------------------------------------------
Sample Input
Guess the secret number: 25
----------------------------------------------------------------
Sample Output
Too low. Try again.
----------------------------------------------------------------
-------------------------------------Coding----------------------------------------
'''
secret_number = 37
print("----------------------------------------------------------------")
while True:
    guess = int(input("Guess the secret number: "))
    if guess < secret_number:
        print("Too low. Try again.")
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        break
print("----------------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------