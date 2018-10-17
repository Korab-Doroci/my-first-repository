'''
This is a login program/form that
i wrote for my first Github repo
'''

# This class runs every time you try to make a new acount
class User:

    # Initazializing password and username when an account is created
    def __init__(self, name, password):
        self.name = name
        self.password = password

    # Shows user what their account name is
    def show_name(self):
        return str("your username is: " + self.name)

    # This function runs every time you try to login
    def loggin(self):

        # Asks user to input their username to login
        loggin_input_name = str(input("input your username here: "))

        # Asks user for the password to their account to login
        loggin_input_password = str(input("input your password here: "))
        
        # Checks if the inputed password is right or wrong
        if loggin_input_name == self.name and \
                loggin_input_password == self.password:
            print("you're logged in as " + self.name)
        else:
            print("the name or password is wrong try again")


# Asks user to make an account and make a username
user_input = input("Create a user\nInput your username: ")
# Asks user to input a password for their account
user_password_input = input("create a password for your account: ")
# Creates a user from the user input
user1 = User(str(user_input), str(user_password_input))
# Automaticly loggin them in to their account
user1.loggin()
