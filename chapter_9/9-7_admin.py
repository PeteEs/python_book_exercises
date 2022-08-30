class User:

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"This is user. This name is {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hi {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):

    def __init__(self,first_name,last_name,privileges = ["can add post","can delete post","can ban user"]):
        super().__init__(first_name,last_name)
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


admin_john = Admin("John","Emm")

admin_john.show_privileges()