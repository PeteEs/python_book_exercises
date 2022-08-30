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

userpete = User("Pete","Error")
userpete.increment_login_attempts()
userpete.increment_login_attempts()
userpete.increment_login_attempts()
userpete.increment_login_attempts()

print(userpete.login_attempts)

userpete.reset_login_attempts()

print(userpete.login_attempts)
