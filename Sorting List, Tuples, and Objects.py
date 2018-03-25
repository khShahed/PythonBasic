
# Sorting list
# li = [5, 2, 1, 7, 9, 8, 6, 3, 4]
# print(li)
# s_li = sorted(li) # Returns new sorted list
# print(s_li)
# li.sort() # sort the list and don't return anything
# print(li)
#
# s_li = sorted(li, reverse=True)
# print(s_li)
# li.sort(reverse=True)
# print(li)

# li = [-6, 4, 0, -2, 9, -5, 7]
# s_li = sorted(li)
# print(li)
# print(s_li)

# li = [-6, 4, 0, -2, 9, -5, 7]
# s_li = sorted(li, key=abs)
# print(li)
# print(s_li)

# -----------------------------------------------------------------
# Sorting Tuple
# tup = (5, 2, 1, 7, 9, 8, 6, 3, 4)
# s_tup = sorted(tup)
# print(tup)
# print(s_tup)

# -----------------------------------------------------------------
# Sorting Dictionary
# dt = {'name':'Kamrul Hasan Shahed', 'age':22,  "test":'Testing'}
# s_dt = sorted(dt)
# print(dt)
# print(s_dt)

# -----------------------------------------------------------------
# Sorting Object

from operator import attrgetter

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return 'Employee({}, {}, {}'.format(self.name, self.age, self.salary)

e1 = Employee("kamrul", 22, 1200)
e2 = Employee("Hasan", 27, 1000)
e3 = Employee("Shahed", 21, 1900)

def e_sort(employee):
    return employee.age

employees = [e1, e2, e3]
# s_employees = sorted(employees, key=e_sort, reverse= True)
# s_employees = sorted(employees, key=lambda e: e.age, reverse= True) # Using lambda
s_employees = sorted(employees, key=attrgetter("age"), reverse= True) # Using attrgetter

print(employees)
print(s_employees)