# Imports
from random import *

# Variables
pasw = 1
start = 1
# Code
  
password = randint(10000, 100000)
print(password)

# Easy|Meduim|Hard|Impossible
choice = input("E|M|H|I:")

if choice == "E":
  while pasw == 1:
    if start == 1:
      print(password)
      start = 0
    passwordguess = int(input("Password:"))
    if password == passwordguess:
      print("Correct!")
      password = randint(1, 10)
      print(password)
      pasw = 1
    elif password > passwordguess:
      print("More")
    elif password < passwordguess:
      print("Less")
    elif password != passwordguess:
      print("Wrong!")
      pasw = 1
      
