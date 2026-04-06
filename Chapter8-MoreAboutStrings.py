# --------------------------------------------
# Name: Natalie Beard
# Date: 4/6/2026
# Program: Chapter 8 Practice
# Description: Practice new string skills
# Complete each section by following the
# directions in the comments.
# --------------------------------------------

# ------------------------------------------------
# Practice 1: Accessing Characters in a String
# ------------------------------------------------
# TODO:
# 1. Create a variable named message and assign it
#    the string: 'Hello, World!'
# 2. Use indexing to print the first character
# 3. Use indexing to print the last character using
#    a negative index
# 4. Use a for loop to print each character in the
#    string on its own line
# 5. Print the total length of the string using len()
print()  # blank line
message = "Hello, World!"
print(message[0])
print(message[-1])
for i in message:
    print(i)
print(len(message))
      
# ------------------------------------------------
# Practice 2: String Slicing and Concatenation
# ------------------------------------------------
# TODO:
# 1. Create a variable named full_name and assign it
#    your first and last name (e.g. 'Jane Smith')
# 2. Use slicing to extract and print just the first name
#    (Hint: slice from 0 up to the index of the space)
# 3. Use slicing to extract and print just the last name
# 4. Create two separate string variables: first and last
#    then concatenate them with a comma and space in between
#    and print the result  (e.g. 'Smith, Jane')
print()
full_name = "Natalie Beard"

first = (full_name[0:7])
last = (full_name[5:-1])
print(first)
print(last)

print(f"{last}.{first}")

      
# ------------------------------------------------
# Practice 3: String Testing Methods
# ------------------------------------------------
# TODO:
# 1. Ask the user to enter a string
# 2. Use isalpha() to check if it contains only letters
#    and print the result
# 3. Use isdigit() to check if it contains only digits
#    and print the result
# 4. Use islower() to check if it is all lowercase
#    and print the result
# 5. Use isupper() to check if it is all uppercase
#    and print the result
print()
user_input = input("Enter a string: ")
                   
print(user_input.isalpha())
print(user_isdigit())
# ------------------------------------------------
# Practice 4: Searching and Manipulating Strings
# ------------------------------------------------
# TODO:
# 1. Create a variable named sentence and assign it:
#    'The quick brown fox jumps over the lazy dog'
# 2. Use lower() to print the sentence in all lowercase
# 3. Use upper() to print the sentence in all uppercase
# 4. Use replace() to replace the word 'fox' with 'cat'
#    and print the result
# 5. Use find() to locate the word 'jumps' and print
#    the index where it starts
# 6. Use startswith() to check if the sentence starts
#    with 'The' and print the result
# 7. Use endswith() to check if the sentence ends
#    with 'dog' and print the result
print()

sentence = "The quick brown fox jumps over the lazy dog"

print(sentence.lower())
print(sentence.upper())
print(sentence.replace('fox', 'cat'))
print(sentence.find('jumps'))
print(sentence.startswith('The'))
print(sentence.endswith('dog'))

# ------------------------------------------------
# Practice 5: Debug the String Program
# ------------------------------------------------
# TODO:
# The program below is supposed to:
# - Take a full name string and split it into parts
# - Print the name in uppercase
# - Check if the name contains only letters and spaces
# - Print each part of the name on its own line
#
# There are 3 errors in this code.
# Fix them so the program works correctly.

full_name = 'marie curie'
name_parts = full_name.split()

print(full_name.upper())

if full_name.replace(' ', '').isalpha():
    print('Contains only letters')

for part in name_parts:
    print(part.capitalize())
print()
