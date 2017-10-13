from time import sleep
import sys
import random

# Variables
login = 0
Username = 0
Password = 0
startcomputer = 0
appopen = 0
# Start Computer
print("Do you want to start the computer?")
startcomputer = input("[y]/[n]:")
if startcomputer == "y":
  text = "Loading ..........."
  for character in text:
    sys.stdout.write(character)
    sleep(0.2)
  login = 1

if startcomputer == "n":
  print("Shutting Down")
  quit()

# Login
if login == 1:
  print("\n" * 1)
  print("Starting Computer")
  Username = input("Username:") 
  Password = input("Password:")
  
# Wrong Login Check
attempts = 1
while Username != "ADMIN" or Password !="ADMIN":
  if attempts >0:
    print("Wrong Username or Password")
    attempts += 1
    Username = input("Username:")
    Password = input("Password:")

# Correct Login Check
if Username == "ADMIN" and Password == "ADMIN":
  print("Successfully Logged In")
  sleep(0.2)
  
  # Opening Apps
  while appopen == 0:
    print("What application do you want to open?")
    app = input()
    
    # Chrome
    if app == "email":
      print("Opening Email")
      emailchoice = input()
      if emailchoice == "send"
        print("What email address?")
        emailaddress = input()
      appopen = 1
      
    # Application not found  
    else:
      print("Application not found")
      appopen = 0
      
    # Application closed
    if appopen == 1:
      print("Application Closed")
      appopen =  0
      
