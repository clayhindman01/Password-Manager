from password_manager import PasswordManager
import sys

def main():

    #Ask the user for its name and check with the masterpassword on file,
    #If the name doesn't match the password offer to create a name-password combonation
    name = input("Enter your name: ")
    master = input("Enter the masterpassword for %s: " % name)
    
    if verifyMasterPassword(name, master):
        if sys.argv[1] == "add":
            website = input("What website do you want your username and password saved for? ")
            username = input("Enter your username for %s: " % website)
            password = input("Enter your password for %s: " % website)
            
            pm = PasswordManager(name, website, username, password)

# TODO Verify that the master password is the correct on for that user.
def verifyMasterPassword(name, master_password):
    if master_password == "Test":
        return True
    else: 
        return False

main()