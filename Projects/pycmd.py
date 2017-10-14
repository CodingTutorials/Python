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
  if admin == 0:
    print("Please Login To Enable All Features")
  command = input("Command:")
  
  # Help
  if command == "help":
    if admin == 1:
      print("Commands: time, passgen, email, github, google")
      cmd = 0
    else:
      print("Login by typing login")
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
        
  # Time
  if command == "time":
    if admin == 1:
      time = datetime.datetime.now()
      print("Enter [y],[m],[d],[h],[min]")
      timeformat = input("Time Format:")
      if timeformat == "y":
        print(time.year)
        cmd = 0
      if timeformat == "m":
        print(time.month)
        cmd = 0
      if timeformat == "d":
        print(time.day)
        cmd = 0
      if timeformat == "h":
        print(time.hour)
        cmd = 0
      if timeformat == "min":
        print(time.minute)
        cmd = 0
    else:
      print("You need to login")
      cmd = 0
      
  # Password Generater
  if command == "passgen":
    if admin == 1:
      print("How many passwords do you want?")
      passgenamount = int(input("Passwords:"))  
      for x in range(passgenamount):
        print (random.randint(10000000,100000000))
      cmd = 0
    else:
      print("You need to login")
      cmd = 0

  # Email
  if command == "email":
    if admin == 1:
      print("What email address?")
      address = input("Address:")
      print("What subject?")
      subject = input("Subject:")
      print("What message?")
      message = input("Message:")
      print("Sent to:",address,"Subject:",subject,"Message:",message)
      cmd = 0
    else:
      print("You need to login")
      cmd = 0
  
  # GitHub
  if command == "github":
    if admin == 1:
      print("What do you want to search for?")
      githubsearch = input("Search:")
      print("Go to: https://github.com/search?utf8=%E2%9C%93&q=",githubsearch,"&type=", sep='')
      cmd = 0
    else:
      print("You need to login")
      cmd = 0
  
  # Google
  if command == "google":
    if admin == 1:
      print("What do you want to search for?")
      googlesearch = input("Search:")
      print("https://www.google.com/search?&q=",googlesearch, sep = '')
      cmd = 0
    else:
      print("You need to login")
      cmd = 0
  # Command Finished
  if cmd == 0:
    print("Command Finished")
    cmd = 1
    
  # Command Not Found
  else:
    print(command,"is not a command")
