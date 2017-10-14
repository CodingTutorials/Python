# Imports 
from time import sleep
import random
import datetime
# Variables
cmd = 1

# Command
while cmd == 1:
  command = input("Command:")
  
  # Time
  if command == "time":
    time = datetime.datetime.now()
    print(time.year)
    cmd = 0
  # Pass Gen
  if command == "passgen":
    print("How many passwords do you want?")
    passgenamount = int(input("Passwords:"))  
    for x in range(passgenamount):
      print (random.randint(10000000,100000000))
    cmd = 0
  if cmd == 0:
    print("Command Executed")
    cmd = 1
  else:
    print(command,"is not a command")
