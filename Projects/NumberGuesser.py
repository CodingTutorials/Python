# Number Guesser
# Created by Nathan R (Mosrod) https://github.com/Mosrod

# Imports
from random import *
from time import sleep
import sys

# Variables
pasw = 1
start = 1
number = 0
diff = 1
guesscount = 1
less = 1
streakcount = 0
streakguess = 0
streak1 = 0
streak2 = 0
streak3 = 0
# Prints All Numbers (Change to dev = 1 to enable)
dev = 0

# Code
if start == 1:
  text = "Welcome to Number Guesser"
  for character in text:
    sys.stdout.write(character)
    sleep(0.1)
  print("\n")
  text = "Created by Nathan R (Mosrod)"
  for character in text:
    sys.stdout.write(character)
    sleep(0.05)
  print("\n")
  text = "|Easy|Medium|Hard|VeryHard|Extreme|Impossible|Impossible2|Impossible3|Custom|Learn|"
  for character in text:
    sys.stdout.write(character)
    sleep(0.02)
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
        number = randint(1, 10)
        print("Easy Mode is |between 1 and 10| and |has a streak of 3|")
        if dev == 1:
          print(number)
        start = 0
      numberguess = int(input("Number:"))
      if number == numberguess:
        print("Correct!")
        print("You guessed the number in", guesscount, "tries")
        streakcount += 1
        streakguess += guesscount
        if streak1 > 3 or streak2 > 3 or streak3 > 3:
          streakcount = 1
        if streakcount == 1:
          streak1 = guesscount
        if streakcount == 2:
          streak2 = guesscount
        if streakcount == 3:
          streak3 = guesscount
          if streak1 <= 3 and streak2 <= 3 and streak3 <= 3:
            print("Streak!")
          else:
            print("No Streak!")
          streak1 = 0
          streak2 = 0
          streak3 = 0
          streakguess = 0
          streakcount = 0
        guesscount = 1
        number = randint(1, 10)
        if dev == 1:
          print(number)
        pasw = 1
      elif number > numberguess:
        print("More")
        guesscount += 1
      elif number < numberguess:
        print("Less")
        guesscount += 1
      elif number != numberguess:
        print("Wrong!")
        pasw = 1
  
  # Medium
  if choice == "M":
    diff = 0
    while pasw == 1:
      if start == 1:
        number = randint(1, 100)
        print("Medium Mode is |between 1 and 100| and |has a streak of 8|")
        if dev == 1:
          print(number)
        start = 0
      numberguess = int(input("Number:"))
      if number == numberguess:
        print("Correct!")
        print("You guessed the number in", guesscount, "tries")
        streakcount += 1
        streakguess += guesscount
        if streak1 > 8 or streak2 > 8 or streak3 > 8:
          streakcount = 1
        if streakcount == 1:
          streak1 = guesscount
        if streakcount == 2:
          streak2 = guesscount
        if streakcount == 3:
          streak3 = guesscount
          if streak1 <= 8 and streak2 <= 8 and streak3 <= 8:
            print("Streak!")
          else:
            print("No Streak!")
          streak1 = 0
          streak2 = 0
          streak3 = 0
          streakguess = 0
          streakcount = 0
        guesscount = 1
        number = randint(1, 100)
        if dev == 1:
          print(number)
        pasw = 1
      elif number > numberguess:
        print("More")
        guesscount += 1
      elif number < numberguess:
        print("Less")
        guesscount += 1
      elif number != numberguess:
        print("Wrong!")
        pasw = 1
  
  # Hard
  if choice == "H":
    diff = 0
    while pasw == 1:
      if start == 1:
        number = randint(1, 1000)
        print("Hard Mode is |between 1 and 1000| and |has a streak of 12|")
        if dev == 1:
          print(number)
        start = 0
      numberguess = int(input("Number:"))
      if number == numberguess:
        print("Correct!")
        print("You guessed the number in", guesscount, "tries")
        streakcount += 1
        streakguess += guesscount
        if streak1 > 12 or streak2 > 12 or streak3 > 12:
          streakcount = 1
        if streakcount == 1:
          streak1 = guesscount
        if streakcount == 2:
          streak2 = guesscount
        if streakcount == 3:
          streak3 = guesscount
          if streak1 <= 12 and streak2 <= 12 and streak3 <= 12:
            print("Streak!")
          else:
            print("No Streak!")
          streak1 = 0
          streak2 = 0
          streak3 = 0
          streakguess = 0
          streakcount = 0
        guesscount = 1
        number = randint(1, 1000)
        if dev == 1:
          print(number)
        pasw = 1
      elif number > numberguess:
        print("More")
        guesscount += 1
      elif number < numberguess:
        print("Less")
        guesscount += 1
      elif number != numberguess:
        print("Wrong!")
        pasw = 1      
  
  # VeryHard
  if choice == "VH":
    diff = 0
    while pasw == 1:
      if start == 1:
        number = randint(1, 10000)
        print("VeryHard Mode is |between 1 and 10000| and |has a streak of 16|")
        if dev == 1:
          print(number)
        start = 0
      numberguess = int(input("Number:"))
      if number == numberguess:
        print("Correct!")
        print("You guessed the number in", guesscount, "tries")
        streakcount += 1
        streakguess += guesscount
        if streak1 > 16 or streak2 > 16 or streak3 > 16:
          streakcount = 1
        if streakcount == 1:
          streak1 = guesscount
        if streakcount == 2:
          streak2 = guesscount
        if streakcount == 3:
          streak3 = guesscount
          if streak1 <= 16 and streak2 <= 16 and streak3 <= 16:
            print("Streak!")
          else:
            print("No Streak!")
          streak1 = 0
          streak2 = 0
          streak3 = 0
          streakguess = 0
          streakcount = 0
        guesscount = 1
        number = randint(1, 10000)
        if dev == 1:
          print(number)
        pasw = 1
      elif number > numberguess:
        print("More")
        guesscount += 1
      elif number < numberguess:
        print("Less")
        guesscount += 1
      elif number != numberguess:
        print("Wrong!")
        pasw = 1
  # Extreme
  if choice == "EX":
    diff = 0
    while pasw == 1:
      if start == 1:
        number = randint(1, 100000)
        print("Extreme Mode is |between 1 and 100000| and |has a streak of 20|")
        if dev == 1:
          print(number)
        start = 0
      numberguess = int(input("Number:"))
      if number == numberguess:
        print("Correct!")
        print("You guessed the number in", guesscount, "tries")
        streakcount += 1
        streakguess += guesscount
        if streak1 > 20 or streak2 > 20 or streak3 > 20:
          streakcount = 1
        if streakcount == 1:
          streak1 = guesscount
        if streakcount == 2:
          streak2 = guesscount
        if streakcount == 3:
          streak3 = guesscount
          if streak1 <= 20 and streak2 <= 20 and streak3 <= 20:
            print("Streak!")
          else:
            print("No Streak!")
          streak1 = 0
          streak2 = 0
          streak3 = 0
          streakguess = 0
          streakcount = 0
        guesscount = 1
        number = randint(1, 100000)
        if dev == 1:
          print(number)
        pasw = 1
      elif number > numberguess:
        print("More")
        guesscount += 1
      elif number < numberguess:
        print("Less")
        guesscount += 1
      elif number != numberguess:
        print("Wrong!")
        pasw = 1
        
  # Impossible
  if choice == "I":
    diff = 0
    while pasw == 1:
      if start == 1:
        number = randint(1, 1000000)
        print("Impossible Mode is |between 1 and 1000000| and |has a streak of 24|")
        if dev == 1:
          print(number)
        start = 0
      numberguess = int(input("Number:"))
      if number == numberguess:
        print("Correct!")
        print("You guessed the number in", guesscount, "tries")
        streakcount += 1
        streakguess += guesscount
        if streak1 > 24 or streak2 > 24 or streak3 > 24:
          streakcount = 1
        if streakcount == 1:
          streak1 = guesscount
        if streakcount == 2:
          streak2 = guesscount
        if streakcount == 3:
          streak3 = guesscount
          if streak1 <= 24 and streak2 <= 24 and streak3 <= 24:
            print("Streak!")
          else:
            print("No Streak!")
          streak1 = 0
          streak2 = 0
          streak3 = 0
          streakguess = 0
          streakcount = 0
        guesscount = 1
        number = randint(1, 1000000)
        if dev == 1:
          print(number)
        pasw = 1
      elif number > numberguess:
        print("More")
        guesscount += 1
      elif number < numberguess:
        print("Less")
        guesscount += 1
      elif number != numberguess:
        print("Wrong!")
        pasw = 1
  
  # Impossible 2
  if choice == "I2":
    diff = 0
    while pasw == 1:
      if start == 1:
        number = randint(1, 10000000)
        print("Impossible2 Mode is |between 1 and 10000000| and |has a streak of 28|")
        if dev == 1:
          print(number)
        start = 0
      numberguess = int(input("Number:"))
      if number == numberguess:
        print("Correct!")
        print("You guessed the number in", guesscount, "tries")
        streakcount += 1
        streakguess += guesscount
        if streak1 > 28 or streak2 > 28 or streak3 > 28:
          streakcount = 1
        if streakcount == 1:
          streak1 = guesscount
        if streakcount == 2:
          streak2 = guesscount
        if streakcount == 3:
          streak3 = guesscount
          if streak1 <= 28 and streak2 <= 28 and streak3 <= 28:
            print("Streak!")
          else:
            print("No Streak!")
          streak1 = 0
          streak2 = 0
          streak3 = 0
          streakguess = 0
          streakcount = 0
        guesscount = 1
        number = randint(1, 10000000)
        if dev == 1:
          print(number)
        pasw = 1
      elif number > numberguess:
        print("More")
        guesscount += 1
      elif number < numberguess:
        print("Less")
        guesscount += 1
      elif number != numberguess:
        print("Wrong!")
        pasw = 1
        
  # Impossible 3
  if choice == "I3":
    diff = 0
    while pasw == 1:
      if start == 1:
        number = randint(1, 100000000)
        print("Impossible3 Mode is |between 1 and 100000000| and |has a streak of 34|")
        if dev == 1:
          print(number)
        start = 0
      numberguess = int(input("Number:"))
      if number == numberguess:
        print("Correct!")
        print("You guessed the number in", guesscount, "tries")
        streakcount += 1
        streakguess += guesscount
        if streak1 > 34 or streak2 > 34 or streak3 > 34:
          streakcount = 1
        if streakcount == 1:
          streak1 = guesscount
        if streakcount == 2:
          streak2 = guesscount
        if streakcount == 3:
          streak3 = guesscount
          if streak1 <= 34 and streak2 <= 34 and streak3 <= 34:
            print("Streak!")
          else:
            print("No Streak!")
          streak1 = 0
          streak2 = 0
          streak3 = 0
          streakguess = 0
          streakcount = 0
        guesscount = 1
        number = randint(1, 100000000)
        if dev == 1:
          print(number)
        pasw = 1
      elif number > numberguess:
        print("More")
        guesscount += 1
      elif number < numberguess:
        print("Less")
        guesscount += 1
      elif number != numberguess:
        print("Wrong!")
        pasw = 1
  
  
  # Custom
  if choice == "C":
    diff = 0
    while pasw == 1:
      if start == 1:
        devx = int(input("X: "))
        devy = int(input("Y: "))
        streakamount = int(input("Streak: "))
        number = randint(devx, devy)
        print("Custom Mode is |between ", devx, " and ", devy,"| and |has a streak of ", streakamount,"|", sep='')
        if dev == 1:
          print(number)
        start = 0
      numberguess = int(input("Number:"))
      if number == numberguess:
        print("Correct!")
        print("You guessed the number in", guesscount, "tries")
        streakcount += 1
        streakguess += guesscount
        if streak1 > streakamount or streak2 > streakamount or streak3 > streakamount:
          streakcount = 1
        if streakcount == 1:
          streak1 = guesscount
        if streakcount == 2:
          streak2 = guesscount
        if streakcount == 3:
          streak3 = guesscount
          if streak1 <= streakamount and streak2 <= streakamount and streak3 <= streakamount:
            print("Streak!")
          else:
            print("No Streak!")
          streak1 = 0
          streak2 = 0
          streak3 = 0
          streakguess = 0
          streakcount = 0
        guesscount = 1
        number = randint(devx, devy)
        if dev == 1:
          print(number)
        pasw = 1
      elif number > numberguess:
        print("More")
        guesscount += 1
      elif number < numberguess:
        print("Less")
        guesscount += 1
      elif number != numberguess:
        print("Wrong!")
        pasw = 1
  
  # Learn
  if choice == "L":
    diff = 0
    while pasw == 1:
      if start == 1:
        number = randint(1, 10)
        if dev == 1:
          print(number)
        print("Choose a number between 1 and 10")
        lesson = 1
        start = 2
      numberguess = int(input("Number:"))
      if number == numberguess:
        print("Correct!")
        print("You guessed the number in", guesscount, "tries")
        if lesson == 1:
          if guesscount <= 5:
            print("You completed the level!")
            guesscount = 1
            lesson = 2
          if guesscount > 5:
            print("You failed the level!")
            print("To complete the level, use less than 5 tries")
            guesscount = 1
            number = randint(1, 10)
            if dev == 1:
              print(number)
            print("Choose a number between 1 and 10")
            
        if lesson == 2:
          if less == 1:
            number = randint(1, 100)
            if dev == 1:
              print(number)
            print("Choose a number between 1 and 100")
            less = 0
          if number == numberguess:
            if guesscount <= 10:
              print("You completed the level!")
              guesscount = 1
              less = 1
              lesson = 3
            if guesscount > 10:
              print("You failed the level!")
              print("To complete the level, use less than 10 tries")
              guesscount = 1
              number = randint(1, 100)
              if dev == 1:
                print(number)
              print("Choose a number between 1 and 100")
        
        if lesson == 3:
          if less == 1:
            number = randint(1, 1000)
            if dev == 1:
              print(number)
            print("Choose a number between 1 and 1000")
            less = 0
          if number == numberguess:
            if guesscount <= 20:
              print("You completed the level!")
              guesscount = 1
              less = 1
              lesson = 4
            if guesscount > 20:
              print("You failed the level!")
              print("To complete the level, use less than 20 tries")
              guesscount = 1
              number = randint(1, 1000)
              if dev == 1:
                print(number)
              print("Choose a number between 1 and 1000")
              
        if lesson == 4:
          if less == 1:
            number = randint(1, 10000)
            if dev == 1:
              print(number)
            print("Choose a number between 1 and 10000")
            less = 0
          if number == numberguess:
            if guesscount <= 40:
              print("You completed the level!")
              guesscount = 1
              less = 1
              lesson = 5
            if guesscount > 40:
              print("You failed the level!")
              print("To complete the level, use less than 40 tries")
              guesscount = 1
              number = randint(1, 10000)
              if dev == 1:
                print(number)
              print("Choose a number between 1 and 10000")
          
        if lesson == 5:
          if less == 1:
            number = randint(1, 100000)
            if dev == 1:
              print(number)
            print("Choose a number between 1 and 100000")
            less = 0
          if number == numberguess:
            if guesscount <= 80:
              print("You completed the level!")
              guesscount = 1
              less = 1
              lesson = 6
            if guesscount > 80:
              print("You failed the level!")
              print("To complete the level, use less than 80 tries")
              guesscount = 1
              number = randint(1, 100000)
              if dev == 1:
                print(number)
              print("Choose a number between 1 and 100000")
              
        if lesson == 6:
          if less == 1:
            number = randint(1, 1000000)
            if dev == 1:
              print(number)
            print("Choose a number between 1 and 1000000")
            less = 0
          if number == numberguess:
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
              number = randint(1, 1000000)
              if dev == 1:
                print(number)
              print("Choose a number between 1 and 1000000")    
              
        guesscount = 1
        if dev == 1:
          print(number)
        pasw = 1
      elif number > numberguess:
        print("More")
        guesscount += 1
      elif number < numberguess:
        print("Less")
        guesscount += 1
      elif number != numberguess:
        print("Wrong!")
        pasw = 1      
  else:
    print("Please Retry")
    diff = 1
