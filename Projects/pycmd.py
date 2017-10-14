# Imports 
from time import sleep
import random
import datetime
# Variables
cmd = 1
username = 1
password = 1
admin = 0
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
    
  # Login  
  if command == "login":
    if username == "admin" and password =="admin":
      print("Already Logged In")
      cmd = 0
    if username != "admin" and password !="admin":
      username = input("Username:")
      password = input("Password:")
      if username == "admin" and password == "admin":
        print("Logged In Successfully")
        admin = 1
        cmd = 0
      if username != "admin" and password !="admin":
        print("Wrong Username or Password")
        cmd = 0
  # Command Finished
  if cmd == 0:
    print("Command Finished")
    cmd = 1
    
  # Command Not Found
  else:
    print(command,"is not a command")
