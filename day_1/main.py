# Strings:
# Strings are encasulated in single or double quotes
# "This is a string"

# If you want to use double quotes in a string, encapsulate the string in single quotes
print('print("Hello World!)')
# Returns:  print("Hello World!)

# Print Function
# print()
print("Hello World")
# Returns:  Hello World

# Adding /n to a string, adds a new line
print("Hello World!\nHello World!\nHello World!")
# Returns:  Hello World!
#           Hello World!
#           Hello World!

# Use + to add (concatenate) two strings together
print("Python" + " " + "Code")
# Returns:  Python Code

# Input Function
# input()
# Gets user input from the console
input("What is your name?")
# Returns:  What is your name? with a prompt for the user to input data

# Combining print and imput functions
print("Hello " + input("What is your name? "))
# Returns:  What is your name? Dave
#           Hello Dave

# Length
# len()
# Counts the number of items in a string
name = "This is a string"
print(len(name))
# Returns 16

# Combining print, imput and len functions
print(len(input("What is your favorite mountain? ")))
# Returns:  What is your favorite mountain? Longs Peak
#           10

# Variables
# Variables allow you to store data to be referenced and manipulated
name = "This is an even longer string"
print(name)
# Returns:  This is an even longer string
# Variables can be reassigned
name = "Short string"
print(name)
# Returns:  This is an even longer string
#           Short string

# Spaces in variable names should be snake case
user_name = input("What is your name? ")
print(user_name)
