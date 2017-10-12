from time import sleep

Username = ""
Password = ""
attempts = 0

while Username != "USER" or Password != "PASS":
  if attempts >0:
    print ("Wrong username or password")
  attempts += 1
  print("What's Username?")
  Username = input()
  print("Whats Password?")
  Password = input()

if Username == "USER" and Password == "PASS":
    print("Starting Computer")
    sleep(1.0)
    print("Loading...")
    sleep(1.0)
    Computer = 1
    Computer_help = 0
    while Computer == 1:
        print("Loading...")
        Computer_help += 1
        sleep(1.0)
        if Computer_help == 4:
            Computer = 2
        while Computer == 2:
            print("Enter Internet")
            inp = input() 
            if inp == "Internet":
                Internet_help = 1
                Computer = 3
                Searchingin = 0
                while Searchingin == 0:
                    if Computer == 3:
                         if inp == "Internet":
                             print("What do you want to search for?")
                             Searching = input()
                             print("Searching for : "+Searching)
                         if Searching == "Google":
                             sleep(1.0)
                             print("Going to Google")
                             Searchingin = 0
                         elif Searching == "List":
                             sleep(1.0)
                             print("Google, Minecraft, Gmail, Shut Down")
                             Searchingin = 0
                         elif Searching == "Shut Down":
                             sleep(1.0)
                             print("Shutting Down")
                             Searchingin = 1
                         elif Searching == "Minecraft":
                             sleep(1.0)
                             print("Opening Minecraft")
                             Searchingin = 0
                         elif Searching == "Gmail":
                             sleep(1.0)
                             print("Opening gmail")
                             gmail = 1
                             Searchingin = 0
                             if gmail == 1:
                                sleep(1.0)
                                print("Enter Send or check")
                                gmail = input()
                                if gmail == "Send":
                                    print("What's email?")
                                    whatsemail = input()
                                    print("What's name?")
                                    whatsname = input()
                                    print("What's message")
                                    whatsmessage = input()
                                    print ("Sending to:",whatsemail,"Name is:",whatsname,"Message:",whatsmessage)
                         else:
                           sleep(1.0)
                           print("No results found, click enter to try again")
                           Searchinginput = input()
                           if Searchingin == "No results found, click enter to try again":
                                 Searchingin = 0
                while Searchingin == 1:
                  print("Shutting Down")
                  Searchingin = 0
                         
