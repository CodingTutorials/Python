# Strings reference guide / tutorial for Python

# Print welcome message
print("Hello World")

# Strings can either be surrounded in " or '
print('Hello World')

# You can use variables to store strings, then print them out
message = "Hello World"
print(message)

# If you want to put single quotes in a single quote string or double quotes in a double quote string, you need to change the string's quote type
# Invalid: 'hello's world'
message = "hello's world"  # Correct

# Invalid: "he said "welcome!""
message = 'he said "welcome!"'  # Correct

# You can also use the backslash character to ignore quotes
message = 'mary\'s ice cream'
message = "she exclaimed \"good\" morning"

# Use three double quotes for a multiline string
message = """ hello
line1
line2
line3
...
"""
print(message)

# Different avaliable functions for strings

# | Length |
a = len("hello") # a = 5
