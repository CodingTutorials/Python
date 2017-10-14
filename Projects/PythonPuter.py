from time import sleep
import sys
import random
def destroy():
  sys.exit()
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
  destroy()

# Login
if login == 1:
  print("\n" * 1)
  print("Starting Computer")
  Username = input("Username:") 
  Password = input("Password:")
  
# Wrong Login Check
attempts = 1
while Username != "admin" or Password !="pass":
  if attempts >0:
    print("Wrong Username or Password")
    attempts += 1
    Username = input("Username:")
    Password = input("Password:")

# Correct Login Check
if Username == "admin" and Password == "pass":
  print("Successfully Logged In")
  sleep(0.2)
  
  # Opening Apps
  while appopen == 0:
    sleep(0.2)
    print("What application do you want to open?")
    app = input()
    
    # Email
    if app == "email":
      print("Opening Email")
      sleep(0.2)
      print("Send or Check")
      emailchoice = input()
      if emailchoice == "send":
        print("What Email Address?")
        emailaddress = input("Email:")
        print("What Subject?")
        emailsubject = input("Subject:")
        print("What Message")
        emailmessage = input("Message:")
        print ("Sending to:",emailaddress,"Subject:",emailsubject,"Message:",emailmessage)
      appopen = 1
      
    # Password Gen
    if app == "passgen":
      print("How many passwords do you want?")
      passgenamount = int(input("Passwords:"))
      for x in range(passgenamount):
        print (random.randint(10000000,100000000))
      appopen =  1
    #log out
    if app == "logout":
      print("logging out...")
      print("please wait...")
      print("Woud you like to Shut Down?")
      shutdown = input("[y]/[n]:")
      if shutdown == "y":
        quit()
      else:
        print("Error #256: No file to cancel shutdown")
    # Application not found  
    else:
      print("Application not found")
      sleep(0.2)
      appopen = 0
      
    # Application closed
    if appopen == 1:
      print("Application Closed")
      sleep(0.2)
      appopen =  0
