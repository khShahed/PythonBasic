
student = {'name':'Kamrul Hasan Shahed', 'age':22, 'courses':['Math', 'Comp Science'], 1:'Testing'}

print(student)
print(student["courses"])
print(student[1])
print(student.get('age'))
print(student.get('agedsfsdf'))
print(student.get('agedsfsdf', "Default value if not found"))

student["phone"] = "782547892"

print(student)

student["name"] = "shahed"

print(student)

student.update({"age":23, "country":"bangladesh"}) # Everythin we want to add or update

print(student)
del student["age"]
print(student)
student.pop("courses")
print(student)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)

for key, value in student.items():
    print("{} --> {}".format(key, value))