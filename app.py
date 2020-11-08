import dbfunctions
import sys

# Allows a user to log in (find a matching username and password combination)
# If the login fails, the user should not be shown the options!
# Once logged in, presents the user with 4 options:
# Enter a new exploit (these are like posts)
# See all of their exploits
# See all other exploits by everyone except for the logged in user
# Exit the application
# The user should be able to re-pick each time (the options should be in a loop)
# Make sure each SQL interaction is supported with the appropriate exception catching.

while True:
    print("1:Login ..")
    print("2: Newuser? Signup..")
    print("3: Exit application.. my exit() or sys.exit() aren't working")
    print("------------------------------------------------------------")
    userChoice = input()
    if userChoice in ('1','2','3'):
        if userChoice == '1':
            username= input("Please type your username: ")
            password= input("Please type your password: ")
            print("------------------------------------------------------------")
            dbfunctions.log_in(username, password)
            while True:
                print("1: Enter a new Exploit")
                print("2: See your exploits")
                print("3: See other hackers exploits")
                print("4: Exit application")
                print("------------------------------")
                menuChoice = input()
                
                if menuChoice == "1":
                    content  = input("Enter your exploit content: ")
                    dbfunctions.insert_data(username, content)
                elif menuChoice == "2":
                    dbfunctions.get_exploit(username)
                elif menuChoice == "3":
                    dbfunctions.get_allexploits(username)
                elif menuChoice == "4":
                     sys.exit()
                
        elif userChoice == '2':
            username= input("Please type your username: ")
            password= input("Please type your password: ")
            dbfunctions.signup(username, password)

        elif userChoice == '3':
            sys.exit()
             