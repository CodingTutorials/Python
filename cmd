import time
import random
import os

print("Please Authenticate Yourself.")
time.sleep(3)
print("Please log in.")
time.sleep(2)
while True:
  
  USER = input("Username")
  PASS = input("Password")
  if USER == "admin":
    if PASS == "admin":
      while True:
        print("Welcome to the command line emulator.")
        print("Type in [help1] for more options")
        while True:
          command = input("admin@pyputer $ ")
          if command == "help1":
            print("""

Help page #1 
 [help1] displays this page 
 
 [man {app}] shows manual for app 
 
 [help2] next page""")
          
          if command == ""
          
          
          
          
          
          
          
          
          
          
          else:
            print("-bash:", command, "is not a command.")
          
    else:
      print("Authentication Failed. Please try again.")
