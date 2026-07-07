'''
---------------------------------------Vowel Counter using Function--------------------------------- 
Write a Python program that defines a function count_vowels(text). 
The function should: 
• Accept a string.  
• Count the total number of vowels (a, e, i, o, u) irrespective of case.  
• Return the total vowel count.  
The main program should: 
• Accept a sentence from the user.  
• Call the function.  
• Display the total number of vowels.  
------------------------------------------------
Sample Input 
Enter a sentence: 
Python Programming is Fun 
------------------------------------------------
Sample Output
Total Vowels: 6
------------------------------------------------
---------------------------------Coding-----------------------------------
'''
# defining the function to count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

#-----------------------main program---------------------------------
print("-----------------------------------------------------------")
text = input("Enter a sentence: ")
print("Total Vowels: ", count_vowels(text))
print("-----------------------------------------------------------")
#------------------------------------------------------------------------------------------------