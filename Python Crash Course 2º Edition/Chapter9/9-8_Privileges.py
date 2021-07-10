class User():
    def __init__(self, first_name, last_name, username, password, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.login_attempts = login_attempts

    def describe_user(self):
        print('\nFull Name: ' + self.first_name.title(), self.last_name.title())
        print('Username: ', self.username)
        print('Password: ',self.password)

    def greet_user(self):
        print('Welcome back to the heel :)')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, username, password, login_attempts=0):
        super().__init__(first_name, last_name, username, password, 
                         login_attempts=login_attempts)
        self.privileges = Privileges()

class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges
    
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

adeemi = Admin('ademaro', 'costa', 'adimir', 'admin1234')
lista_de_privilegios = ['can delete post', 'can fuck all users']
adeemi.privileges.privileges = lista_de_privilegios
adeemi.privileges.show_privileges()
