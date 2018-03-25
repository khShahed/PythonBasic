
class Employee:

    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = self.first+"."+self.last+"@email.com"
        self.pay = pay


    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)

        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        #print("adding ",employee)
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        #print("Removing ",employee)
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        if len(self.employees) == 0:
            return
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for emp in self.employees:
            print("-->", emp.fullname())
        print("---------------------------------")


dev_1 = Developer("Kamrul Hasan", "Shahed", "5000", "Python")
dev_2 = Developer("Test", "Dev", "5000", "Python")

mgr = Manager("Testing","Manager", 90000, [dev_1])
mgr.print_employees()
mgr.add_employee(dev_2)
mgr.print_employees()
mgr.remove_employee(dev_1)
mgr.print_employees()

print(isinstance(mgr, Manager))
print(isinstance(mgr, Developer))
print(isinstance(mgr, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))

# print(dev_1.__dict__)