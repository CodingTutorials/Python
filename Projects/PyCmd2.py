# Imports
from random import *

# Variables
adminuser = "Admin"
adminpass = "Admin"

# Define

# Console
def console():
  command = input(":")

# Login
def login():
  username = input("Username: ")
  password = input("Password: ")
  if username == "Admin" and password == "Admin":
    print("Authentication Success")
    
  elif username == "Guest" and password == "Guest":
    print("Authentication Success")
    
  else:
    print("Authentication Failed")
    
# Number Generator    
def numgen():
  number = randint(1, 10)

  
# Code
print("Welcome to PyCmd 2!")
loginchoice = input("Would you like to login?")


