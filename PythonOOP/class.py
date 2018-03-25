
class Employee:

    raise_amount = 1.04
    number_of_employees = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = self.first+"."+self.last+"@email.com"
        self.pay = pay

        Employee.number_of_employees += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # alternative constructor
    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday == 6:
            return False
        return True

import datetime
my_date = datetime.date(2018, 3, 4)
print(Employee.is_workday(my_date))

# employee_1 = Employee("Kamrul Hasan", "Shahed", 5000)
# employee_2 = Employee("testing", "Employee", 4000)
#
#
# emp = Employee.from_string("Kamrul-Hasan-12000")
# print(emp.__dict__)


# print(employee_1.raise_amount)
# print(employee_2.raise_amount)
# print(Employee.raise_amount)
#
# employee_1.raise_amount = 1.05 # only change for employee_1. It will create a variable for employee_1
#
# Employee.set_raise_amount(1.10) # change raise_amount all excluding instance which already has specific raise_amount variable
#
# print(employee_1.raise_amount)
# print(employee_2.raise_amount)
# print(Employee.raise_amount)

# print(employee_1.__dict__)
# print(employee_2.__dict__)
# print(Employee.__dict__)

# print(employee_1.pay)
# employee_1.apply_raise()
# print(employee_1.pay)


# print(employee1)
# print(employee2)

# print(employee_1.email)
# print(employee_2.email)
#
# print(employee_1.fullname())
# print(employee_2.fullname())
#
#
# print(Employee.fullname(employee_1))
# print(Employee.fullname(employee_2))