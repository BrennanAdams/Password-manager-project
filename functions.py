from xmlrpc.client import Boolean
from cryptography.fernet import Fernet
import bcrypt
import os
import time



passwordMaster = b"password"
hashedPassword = bcrypt.hashpw(passwordMaster, bcrypt.gensalt())

#clear console command, documentation https://www.delftstack.com/howto/python/python-clear-console/
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


clearConsole()

# def writeKey():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as keyFile:
#         keyFile.write(key)

# writeKey()

def quitProgram():
    print("\nQuitting program...")
    time.sleep(.5)
    exit()

def loadKey():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

#function that displays passwords 
def viewPasswords():
    #check if text file exists, if False create a file names password.txt
    pwdIdx = 0
    try:
        with open('passwords.txt', 'r') as f:
            #file is empty
            if (os.stat("passwords.txt").st_size == 0) == True:
                print("File is empty, no password to show\n")
                return False
            else:
                print("Password in database:\n")
                for line in f.readlines():
                        data = line.rstrip()
                        name, password = data.split("|")
                        print( str(pwdIdx) + " | Name: ",fer.decrypt(name.encode()).decode(), "| Password: ",fer.decrypt(password.encode()).decode())
                        print("-----------------------------------------------------")
                        pwdIdx += 1 #adds one to the index for next password in .txt file
                print("\n")

    except FileNotFoundError:
        with open('passwords.txt', 'x') as f:
            print("File not found, creating file name password.txt")
            time.sleep(1.5)
            clearConsole()
            f.close()

#adds password to passwords.txt file
def addPassword(passName, password):
    with open('passwords.txt', 'a') as f:
        #write to end of file
        #format name|password, convert to bytes by using encode, encrypt password, then convert back to string using decode() then add to file
        f.write(str(fer.encrypt(passName.encode()).decode()) + "|" + fer.encrypt(password.encode()).decode() + "\n") 
        print("Adding password...")
        time.sleep(.6)
        clearConsole()

def checkMasterPassword():
    #users enters master password
    while True:
        masterPasswordInput = input("What is the master password or type Q to quit program\n")

        #if user wants to quit
        if masterPasswordInput.lower() == "q":
            quitProgram()

        #encode password
        masterPasswordInput = masterPasswordInput.encode()

        if bcrypt.checkpw(masterPasswordInput, hashedPassword):
            #matches
            print("Correct password\n")
            time.sleep(.5)
            clearConsole()
            return True
        else:
            #ask for password again, print wrong passsword
            print("Wrong password!\n")
            continue


def deletePassword():
    #print the current list of passwords
    if viewPasswords() == False: 
        return False

    lines = []
    # read file
    with open("passwords.txt", 'r') as fp:
        # read an store all lines into list
        lines = fp.readlines()
        fileLength = enumerate(lines)
    
    #ask for user input on which password to remove
    while True:
        removedIdx = input("Please select password index you want to delete: ")
        #check if input is valid
        if removedIdx.isalpha():
            print("Please enter a valid input!\n")
            continue
        elif int(removedIdx) < 0:
            print("Please enter a valid input!\n")
            continue
        else:
            #user enters valid input
            break

    
        # list to store file lines
    

    
    removedIdx = int(removedIdx)
    # Write file
    with open("passwords.txt", 'w') as fp:
        # iterate each line
        for number, line in fileLength:
            #if the current line index is not the one we want to delete, add it to the file
            if number not in [removedIdx, removedIdx]:
                fp.write(line)


key = loadKey()
fer = Fernet(key) #init for decrypting and encypting normal passwords