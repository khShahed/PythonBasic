

courses = ["History", "Math", "Computer Science", "Physics"]
courses_2 = ["Test 1", "Test 2"]
print(courses)
courses.append("Art")
print(courses)
courses.insert(0,"Buscom")
print(courses)
courses.extend(courses_2)
print(courses)

courses.remove("History")
print(courses)
courses.pop() # remove last value
print(courses)
courses.reverse()
print(courses)
courses.sort()
print(courses)
courses.sort(reverse=True)
print(courses)

sorted = sorted(courses)
print(sorted)
print(courses)
print(min(courses))

print("Art" in courses)
print("History" in courses)

for index, course in enumerate(courses, start=1):
    print("{0:03} -> {1:>25}".format(index, course))

print(", ".join(courses))