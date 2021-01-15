#! Python 3.9.1
#Creates a password manager that is run through command promt 

# TODO Connect to a database and learn to retrieve data from it

class PasswordManager():
    """
    Class for the password manager
    """

    #Init for the PasswordManager class
    def __init__(self, name, website = "", username = "", password = ""):
        
        self.name = name
        self.website = website
        self.username = username
        self.password = password

    # TODO Create User-masterpassword link
    def createMasterPassword(self):
        pass

    # TODO Store website and password together
    def storePassword(self):
        pass

    # TODO Retrieve all the websites and usernames and passwords that are stored.
    def getPassword(self):
        pass


