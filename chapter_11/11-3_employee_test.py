import unittest
from employee_class import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.salary = 100000
        self.my_employee = Employee("John","Wick",self.salary)
        self.default_rise = 5000
        self.custom_rise = 10000

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.ann_salary,self.salary + self.default_rise)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(self.custom_rise)
        self.assertEqual(self.my_employee.ann_salary,self.salary + self.custom_rise)

if __name__ == '__main__':
    unittest.main()