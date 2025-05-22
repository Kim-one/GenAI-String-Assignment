# Assignment 3: This assignment focuses on strings
# 

# Task 1: String Slicing and Indexing
string = 'Python is amazing!'

print(f"First word: {string[0:6]}") # prints the first 6 characters
print(f"Amazing part: {string[9:17]}") # prints the word amazing from the string 
print(f"Reversed String: {string[::-1]}") # reverses the string

# Task 2: String Methods 
string = " hello, python world!"

print(f"{string.strip()}") # Removes extra spaces
print(f"{string.strip().capitalize()}") # Removes the extra space then capitalize the first word
print(f"{string.replace("world", "universe")}") # replaces 'world' with 'universe in the string
print(f"{string.upper()}") # changes the entire string from upper case to lower case

# Task 3: Palindromes
# Checks if a word is a palindrome

word = input("Enter a word: ") # gets user input

if word[::-1] == word: # reverses a string and checks if it's still equal to the word 
    # prints a confirmation message
    print(f"Yes, '{word}' is a palindrome!") 
else: 
    print(f"No, '{word}' is not a palindrome")