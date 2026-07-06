'''
---------------------------------------------Word Frequency Counter----------------------------------------- 
Problem Statement: 
Accept a sentence from the user and create a dictionary that stores the frequency of each word. 
Example: 
------------------------------------------------
Sample input: 
python is easy and python is powerful 
------------------------------------------------
Output: 
{ 
'python': 2, 
'is': 2, 
'easy': 1, 
'and': 1, 
'powerful': 1 
} 
------------------------------------------------
Additionally: 
• Display the most frequently occurring word.  
• Display all words in alphabetical order.  
---------------------------------------------------------------------------------------------------------
----------------------------------------------Coding------------------------------------------
'''

# Accept a sentence from the user
sentence = input("Enter a sentence: ")
words = sentence.lower().split()

# Create frequency dictionary
word_frequency = {}
for word in words:
	if word in word_frequency:
		word_frequency[word] = word_frequency[word] + 1
	else:
		word_frequency[word] = 1

print("-------------------------------------------------")
print(word_frequency)

# Display the most frequently occurring word
most_frequent_word = max(word_frequency, key=word_frequency.get)
print("Most Frequently Occurring Word:", most_frequent_word)
print("Frequency:", word_frequency[most_frequent_word])

# Display all words in alphabetical order
print("-------------------------------------------------")
print("Words in Alphabetical Order:")
for word in sorted(word_frequency):
	print(word, ":", word_frequency[word])
print("-------------------------------------------------")
#----------------------------------------------------------------------------------------------------------