# Grade Converter
# Created by Nathan R (Mosrod) https://github.com/Mosrod
# Grading based on http://cs.smith.edu/~jorourke/Grading.html

# Imports
from time import sleep
import sys

# Variables
ask = 1

# Definitions

# Checker
def checker():
  
  if Score >= 97.5:
    print("A+")
  
  elif Score >= 92.5:
    print("A")
  
  elif Score >= 90.0:
    print("A-")
  
  elif Score >= 87.5:
    print("B+")
  
  elif Score >= 82.5:
    print("B")
  
  elif Score >= 80.0:
    print("B-")
  
  elif Score >= 77.5:
    print("C+")
  
  elif Score >= 72.5:
    print("C")
  
  elif Score >= 70.0:
    print("C-")
  
  elif Score >= 67.5:
    print("D+")
  
  elif Score >= 62.5:
    print("D")
    
  elif Score >= 60.0:
    print("D-")
    
  elif Score < 60.0:
    print("F")

# Code
text = "Welcome to Grade Converter"
for character in text:
  sys.stdout.write(character)
  sleep(0.05)
print("\n")
text = "Created by Nathan R (Mosrod)"
for character in text:
  sys.stdout.write(character)
  sleep(0.03)
print("\n")

while ask == 1:
  Choice = input("Fraction/Percent [F/P]:")
  ask = 0

  if Choice == "F" or Choice == "f":
    Numerator = float(input("Points: "))
    Denominator = float(input("Total: "))
    Score = Numerator/Denominator * 100
    checker()
  
  if Choice == "P" or Choice == "p":
    Score = float(input("Percent: "))
    checker()
  
  else:
    ask = 1
