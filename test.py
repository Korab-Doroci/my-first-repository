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


user_input = input("what is your name? ")

user_password_input = input("create a password for your account")

user1 = User(str(user_input), str(user_password_input))
