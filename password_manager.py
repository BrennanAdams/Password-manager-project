from xmlrpc.client import Boolean
from cryptography.fernet import Fernet
import bcrypt
import os
import time
import functions



print("Welcome to the password manager\n")

#while user doesnt enter valid password
functions.checkMasterPassword()

while True:
    print("****** Menu ******")
    print("Enter 0 to enter a new password\nEnter 1 to view existing passwords\nEnter 2 to delete a password\nEnter 9 to quit program\n")

    uInput = int(input("Input: "))


    #check if user input is valid
    if uInput != 0 and uInput != 1 and uInput != 9 and uInput != 2:
        print("Please enter valid option!")
        time.sleep(.2)
        functions.clearConsole()
        continue

    #user quits
    if uInput == 9:
        functions.quitProgram()
    #user wants to view passwords
    elif uInput == 1:
        functions.clearConsole()
        functions.viewPasswords()
    #user wants to add password
    elif uInput == 0:
        #ask for name and password then pass to add password function
        passName = input("Please enter account name: ")
        password = input("Please enter password: ")

        functions.addPassword(passName,password)
    elif uInput == 2:
        #user wants to delete password from system
        functions.clearConsole()
        functions.deletePassword()