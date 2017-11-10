# Imports
from random import *
from time import sleep
import sys

# Variables
pasw = 1
start = 1
password = 0
diff = 1
guesscount = 1
less = 1
# Prints All Passwords (Change to dev = 1 to enable)
dev = 0

# Code
if start == 1:
  text = "Welcome to Password Guesser!"
  for character in text:
    sys.stdout.write(character)
    sleep(0.2)
  print("\n")
  text = "|Easy|Medium|Hard|VeryHard|Extreme|Impossible|Impossible2|Impossible3|Custom|Learn|"
  for character in text:
    sys.stdout.write(character)
    sleep(0.05)
  print("\n")
if dev == 1:
  text = "You are a developer!"
  for character in text:
    sys.stdout.write(character)
    sleep(0.05)
  print("\n")
# |Easy(1-10)|Medium(1-100)|Hard(1-100)|VeryHard(1-1000)|Extreme(1-10000)|Impossible(1-100000)|Impossible2(1-1000000)|Impossible3(1-100000000)Custom|Learn|
while diff == 1:
  choice = input("|E|M|H|VH|EX|I|I2|I3|C|L|:")
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

# VeryHard
if choice == "VH":
  diff = 0
  while pasw == 1:
    if start == 1:
      password = randint(1, 10000)
      print("VeryHard Mode is between 1 and 10000")
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
# Extreme
if choice == "EX":
  diff = 0
  while pasw == 1:
    if start == 1:
      password = randint(1, 100000)
      print("Extreme Mode is between 1 and 100000")
      start = 0
    passwordguess = int(input("Password:"))
    if password == passwordguess:
      print("Correct!")
      print("You guessed the password in", guesscount, "tries")
      guesscount = 0
      password = randint(1, 100000)
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
      password = randint(1, 1000000)
      print("Impossible Mode is between 1 and 1000000")
      start = 0
    passwordguess = int(input("Password:"))
    if password == passwordguess:
      print("Correct!")
      print("You guessed the password in", guesscount, "tries")
      guesscount = 0
      password = randint(1, 1000000)
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

# Impossible 2
if choice == "I2":
  diff = 0
  while pasw == 1:
    if start == 1:
      password = randint(1, 10000000)
      print("Impossible2 Mode is between 1 and 10000000")
      start = 0
    passwordguess = int(input("Password:"))
    if password == passwordguess:
      print("Correct!")
      print("You guessed the password in", guesscount, "tries")
      guesscount = 0
      password = randint(1, 10000000)
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
      
# Impossible 3
if choice == "I3":
  diff = 0
  while pasw == 1:
    if start == 1:
      password = randint(1, 100000000)
      print("Impossible3 Mode is between 1 and 100000000")
      start = 0
    passwordguess = int(input("Password:"))
    if password == passwordguess:
      print("Correct!")
      print("You guessed the password in", guesscount, "tries")
      guesscount = 0
      password = randint(1, 100000000)
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
      if dev == 1:
        print(password)
      print("Choose a number between 1 and 10")
      lesson = 1
      start = 2
    passwordguess = int(input("Password:"))
    if password == passwordguess:
      print("Correct!")
      print("You guessed the password in", guesscount, "tries")
      if lesson == 1:
        if guesscount <= 5:
          print("You completed the level!")
          guesscount = 1
          lesson = 2
        if guesscount > 5:
          print("You failed the level!")
          print("To complete the level, use less than 5 tries")
          guesscount = 1
          password = randint(1, 10)
          if dev == 1:
            print(password)
          print("Choose a number between 1 and 10")
          
      if lesson == 2:
        if less == 1:
          password = randint(1, 100)
          if dev == 1:
            print(password)
          print("Choose a number between 1 and 100")
          less = 0
        if password == passwordguess:
          if guesscount <= 10:
            print("You completed the level!")
            guesscount = 1
            less = 1
            lesson = 3
          if guesscount > 10:
            print("You failed the level!")
            print("To complete the level, use less than 10 tries")
            guesscount = 1
            password = randint(1, 100)
            if dev == 1:
              print(password)
            print("Choose a number between 1 and 100")
      
      if lesson == 3:
        if less == 1:
          password = randint(1, 1000)
          if dev == 1:
            print(password)
          print("Choose a number between 1 and 1000")
          less = 0
        if password == passwordguess:
          if guesscount <= 20:
            print("You completed the level!")
            guesscount = 1
            less = 1
            lesson = 4
          if guesscount > 20:
            print("You failed the level!")
            print("To complete the level, use less than 20 tries")
            guesscount = 1
            password = randint(1, 1000)
            if dev == 1:
              print(password)
            print("Choose a number between 1 and 1000")
            
      if lesson == 4:
        if less == 1:
          password = randint(1, 10000)
          if dev == 1:
            print(password)
          print("Choose a number between 1 and 10000")
          less = 0
        if password == passwordguess:
          if guesscount <= 40:
            print("You completed the level!")
            guesscount = 1
            less = 1
            lesson = 5
          if guesscount > 40:
            print("You failed the level!")
            print("To complete the level, use less than 40 tries")
            guesscount = 1
            password = randint(1, 10000)
            if dev == 1:
              print(password)
            print("Choose a number between 1 and 10000")
        
      if lesson == 5:
        if less == 1:
          password = randint(1, 100000)
          if dev == 1:
            print(password)
          print("Choose a number between 1 and 100000")
          less = 0
        if password == passwordguess:
          if guesscount <= 80:
            print("You completed the level!")
            guesscount = 1
            less = 1
            lesson = 6
          if guesscount > 80:
            print("You failed the level!")
            print("To complete the level, use less than 80 tries")
            guesscount = 1
            password = randint(1, 100000)
            if dev == 1:
              print(password)
            print("Choose a number between 1 and 100000")
            
      if lesson == 6:
        if less == 1:
          password = randint(1, 1000000)
          if dev == 1:
            print(password)
          print("Choose a number between 1 and 1000000")
          less = 0
        if password == passwordguess:
          if guesscount <= 160:
            print("You completed the level!")
            print("You completed Learn Mode!")
            print("Try Custom Mode if you want to make your own range")
            guesscount = 1
            less = 1
            lesson = 0
          if guesscount > 160:
            print("You failed the level!")
            print("To complete the level, use less than 160 tries")
            guesscount = 1
            password = randint(1, 1000000)
            if dev == 1:
              print(password)
            print("Choose a number between 1 and 1000000")    
            
      guesscount = 1
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
