class User:

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"This is user. This name is {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hi {self.first_name}!")


user_1 = User("Stephen","Wick")
user_2 = User("Ann","Choo")

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()
