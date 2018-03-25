
class Employee:

    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = self.first.replace(" ",".")+"."+self.last+"@email.com"
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __repr__(self):
        return "Employee('{}','{}', {})".format(self.first, self.last, self.pay)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

employee_1 = Employee("Kamrul Hasan", "Shahed", 5000)
employee_2 = Employee("testing", "Employee", 4000)

print(employee_1 + employee_2)
print(len(employee_2))
print(len(employee_1))

# print(employee_1)
# print(repr(employee_1))
# print(str(employee_1))
#
# print(employee_1.__repr__())