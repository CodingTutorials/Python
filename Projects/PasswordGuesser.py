# Imports
from random import *

# Variables
pasw = 1
start = 1
password = 0
diff = 1
guesscount = 1
# Prints All Passwords (Change to dev = 1 to enable)
dev = 0
# Code
if start == 1:
  print("Welcome to Password Guesser!")
  print("|Easy|Meduim|Hard|Impossible|Custom|")
if dev == 1:
  print("You are a developer!")
# |Easy|Meduim|Hard|Impossible|Custom|
while diff == 1:
  choice = input("|E|M|H|I|C|:")
  diff = 0

# Easy
if choice == "E":
  diff = 0
  while pasw == 1:
    if start == 1:
      print(password)
      start = 0
    passwordguess = int(input("Password:"))
    if password == passwordguess:
      print("Correct!")
      print("You guessed the password in", guesscount, "tries")
      guesscount = 0
      password = randint(1, 10)
      if dev == 1:
        print(password)
      pasw = 1
    elif password > passwordguess:
      print("More")
      guesscount += 1
    elif password < passwordguess:
      print("Less")
      guesscount += 1
    elif password != passwordguess:
      print("Wrong!")
      pasw = 1

# Meduim
if choice == "M":
  diff = 0
  while pasw == 1:
    if start == 1:
      print(password)
      start = 0
    passwordguess = int(input("Password:"))
    if password == passwordguess:
      print("Correct!")
      print("You guessed the password in", guesscount, "tries")
      guesscount = 0
      password = randint(1, 100)
      if dev == 1:
        print(password)
      pasw = 1
    elif password > passwordguess:
      print("More")
      guesscount += 1
    elif password < passwordguess:
      print("Less")
      guesscount += 1
    elif password != passwordguess:
      print("Wrong!")
      pasw = 1

# Hard
if choice == "H":
  diff = 0
  while pasw == 1:
    if start == 1:
      print(password)
      start = 0
    passwordguess = int(input("Password:"))
    if password == passwordguess:
      print("Correct!")
      print("You guessed the password in", guesscount, "tries")
      guesscount = 0
      password = randint(1, 1000)
      if dev == 1:
        print(password)
      pasw = 1
    elif password > passwordguess:
      print("More")
      guesscount += 1
    elif password < passwordguess:
      print("Less")
      guesscount += 1
    elif password != passwordguess:
      print("Wrong!")
      pasw = 1      

# Impossible
if choice == "I":
  diff = 0
  while pasw == 1:
    if start == 1:
      print(password)
      start = 0
    passwordguess = int(input("Password:"))
    if password == passwordguess:
      print("Correct!")
      print("You guessed the password in", guesscount, "tries")
      guesscount = 0
      password = randint(10000, 100000)
      if dev == 1:
        print(password)
      pasw = 1
    elif password > passwordguess:
      print("More")
      guesscount += 1
    elif password < passwordguess:
      print("Less")
      guesscount += 1
    elif password != passwordguess:
      print("Wrong!")
      pasw = 1
      
# Custom
if choice == "C":
  diff = 0
  while pasw == 1:
    if start == 1:
      print(password)
      start = 0
    passwordguess = int(input("Password:"))
    if password == passwordguess:
      print("Correct!")
      guesscount = 0
      print("You guessed the password in", guesscount, "tries")
      devx = int(input("X: "))
      devy = int(input("Y: "))
      password = randint(devx, devy)
      if dev == 1:
        print(password)
      pasw = 1
    elif password > passwordguess:
      print("More")
      guesscount += 1
    elif password < passwordguess:
      print("Less")
      guesscount += 1
    elif password != passwordguess:
      print("Wrong!")
      pasw = 1
      
else:
  print("Please Retry")
