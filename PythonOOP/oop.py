
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return self.first.replace(" ",".")+"."+self.last+"@email.com"

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(" ")

    @fullname.deleter
    def fullname(self):
        print("Deleting fullname...")
        self.first = None
        self.last = None


employee_1 = Employee("testing", "Employee")

employee_1.fullname = "Hello World"

print(employee_1.first)
print(employee_1.fullname)
print(employee_1.email)

del employee_1.fullname

print(employee_1.fullname)
