class Employee:

    def __init__(self,first_name,last_name,ann_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.ann_salary = ann_salary

    def give_raise(self,amount=5000):
        self.ann_salary += amount

