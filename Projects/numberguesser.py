# Imports
from random import *

# Variables
pasw = 1
start = 1
password = 0
# Prints All Passwords (Change to dev = 1 to enable)
dev = 0
# Code
  
# password = randint(10000, 100000)
# print(password)

# Easy|Meduim|Hard|Impossible
choice = input("E|M|H|I:")

# Easy
if choice == "E":
  while pasw == 1:
    if start == 1:
      print(password)
      start = 0
    passwordguess = int(input("Password:"))
    if password == passwordguess:
      print("Correct!")
      password = randint(1, 10)
      if dev == 1:
        print(password)
      pasw = 1
    elif password > passwordguess:
      print("More")
    elif password < passwordguess:
      print("Less")
    elif password != passwordguess:
      print("Wrong!")
      pasw = 1

# Meduim
if choice == "M":
  while pasw == 1:
    if start == 1:
      print(password)
      start = 0
    passwordguess = int(input("Password:"))
    if password == passwordguess:
      print("Correct!")
      password = randint(1, 100)
      if dev == 1:
        print(password)
      pasw = 1
    elif password > passwordguess:
      print("More")
    elif password < passwordguess:
      print("Less")
    elif password != passwordguess:
      print("Wrong!")
      pasw = 1

# Hard
if choice == "H":
  while pasw == 1:
    if start == 1:
      print(password)
      start = 0
    passwordguess = int(input("Password:"))
    if password == passwordguess:
      print("Correct!")
      password = randint(1, 1000)
      if dev == 1:
        print(password)
      pasw = 1
    elif password > passwordguess:
      print("More")
    elif password < passwordguess:
      print("Less")
    elif password != passwordguess:
      print("Wrong!")
      pasw = 1      

# Impossible
if choice == "I":
  while pasw == 1:
    if start == 1:
      print(password)
      start = 0
    passwordguess = int(input("Password:"))
    if password == passwordguess:
      print("Correct!")
      password = randint(10000, 100000)
      if dev == 1:
        print(password)
      pasw = 1
    elif password > passwordguess:
      print("More")
    elif password < passwordguess:
      print("Less")
    elif password != passwordguess:
      print("Wrong!")
      pasw = 1
