
# person = {"name": "Kamrul Hasan Shahed", 'age': 22 }
# li = ['Kamrul Hasan Shahed', 22]
#
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p = Person("Shahed", 22)
#
# print("My name is {} and I'm {} years old.".format(person["name"], person["age"]))
# print("My name is {0[name]} and I'm {1[age]} years old.".format(person, person))
# print("My name is {0[name]} and I'm {0[age]} years old.".format(person))
# print("My name is {name} and I'm {age} years old.".format(**person))
#
# print("My name is {0[0]} and I'm {0[1]} years old.".format(li))
#
# print("My name is {0.name} and I'm {0.age} years old.".format(p))
#
# print("My name is {name} and I'm {age} years old.".format(name="Shahed", age=22))
#
# tag = "h1"
# text = "This is a heading"
# print("<{0}>{1}</{0}".format(tag, text))

# for i in range(1, 11):
#     print("{:02}".format(i))

# pi = 3.14159265
# print('Pi is equal to {:.4f}'.format(pi))

print("1 MB is equal to {:,.2f} bytes".format(1000**2))

# ---------------------- DATES ------------------
import datetime

my_date = datetime.datetime.now()
print("{:%B %d, %Y}".format(my_date))
print("{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year.".format(my_date))