from employee import Employee
import unittest


class TestEmpolyee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('xinhan', 'niu', 5000)

    def test_give_deefault_raise(self):
        salary = self.employee.salary
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, salary + 5000)

    def test_give_custom_raise(self):
        salary = self.employee.salary
        self.employee.give_raise(2000)
        self.assertEqual(self.employee.salary, salary + 2000)


if __name__ == '__main__':
    unittest.main()