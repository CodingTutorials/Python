# Imports
from random import *

# Variables
pasw = 1
start = 1
password = 0
diff = 1
guesscount = 0
# Prints All Passwords (Change to dev = 1 to enable)
dev = 0

# Code
if start == 1:
  print("Welcome to Password Guesser!")
  print("|Easy|Medium|Hard|Impossible|Custom|Learn|")
if dev == 1:
  print("You are a developer!")
# |Easy|Medium|Hard|Impossible|Custom|Learn|
while diff == 1:
  choice = input("|E|M|H|I|C|L|:")
  diff = 0

# Easy
if choice == "E":
  diff = 0
  while pasw == 1:
    if start == 1:
      password = randint(1, 10)
      print("Easy Mode is between 1 and 10")
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

# Medium
if choice == "M":
  diff = 0
  while pasw == 1:
    if start == 1:
      password = randint(1, 100)
      print("Medium Mode is between 1 and 100")
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
      password = randint(1, 1000)
      print("Hard Mode is between 1 and 1000")
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
      password = randint(1, 10000)
      print("Impossible Mode is between 1 and 10000")
      start = 0
    passwordguess = int(input("Password:"))
    if password == passwordguess:
      print("Correct!")
      print("You guessed the password in", guesscount, "tries")
      guesscount = 0
      password = randint(1, 10000)
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
      devx = int(input("X: "))
      devy = int(input("Y: "))
      password = randint(devx, devy)
      print("Custom Mode is between", devx, "and", devy)
      start = 0
    passwordguess = int(input("Password:"))
    if password == passwordguess:
      print("Correct!")
      print("You guessed the password in", guesscount, "tries")
      guesscount = 0
      devx = int(input("X: "))
      devy = int(input("Y: "))
      print("Custom Mode is between", devx, "and", devy)
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

# Learn
if choice == "L":
  diff = 0
  while pasw == 1:
    if start == 1:
      password = randint(1, 10)
      print("Choose a number between 1 and 10")
      lesson = 1
      start = 2
    passwordguess = int(input("Password:"))
    if password == passwordguess:
      print("Correct!")
      print("You guessed the password in", guesscount, "tries")
      if lesson == 1:
        if guesscount < 5:
          print("You completed the level!")
          lesson = 2
        if guesscount > 5:
          print("You failed the level!")
          print("To complete the level, use less than 5 tries")
          password = randint(1, 10)
          print("Choose a number between 1 and 10")
      guesscount = 0
      if lesson == 2:
        password = randint(1, 100)
        print("Choose a number between 1 and 100")
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
