import time
import random
import os
def passgen():
  print("How many passwords do you want?")
  passgenamount = int(input("Passwords:"))
  for x in range(passgenamount):
    print (random.randint(10000000,100000000))


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
 
 [passgen] generates secure 8 digit passwords
 
 [man {app}] shows manual for app 
 
 [help2] next page""")
          
          if command == "pass-gen":
            passgen()
          
          if command == "man pass-gen":
            print("""Manual page for Passgen
            passgen is a free open-source application included in the pyputer operating system. It generates a random password that is 8 digit long and secure. To use it, type in pass-gen and the file will execute.""")
          
          

          
          
          
          else:
            print("-bash:", command, "is not a command")
          
    else:
      print("Authentication Failed. Please try again.")
