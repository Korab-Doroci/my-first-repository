'''
det här är ett program jag
skrev för mitt första github repo
'''


class User:

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def show_name(self):
        return str("this users name is: " + self.name)

    def loggin(self):
        loggin_input_name = str(input("input your username here "))
        loggin_input_password = str(input("input your password here "))

        if loggin_input_name == self.name and \
                loggin_input_password == self.password:
            print("your logged in as " + self.name)
        else:
            print("the name or password is wrong try again ")


user_input = input("what is your name? ")

user_password_input = input("create a password for your account ")

user1 = User(str(user_input), str(user_password_input))

user1.loggin()
