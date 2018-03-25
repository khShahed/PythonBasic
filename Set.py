

courses = {"History", "Math", "Computer Science", "Physics"}
courses_2 = {"Art", "Math", "Computer Science", "Design"}

print(courses)
courses.add("Math")
print(courses)
print("Math" in courses)

print(courses.intersection(courses_2))
print(courses.difference(courses_2))
print(courses.union(courses_2))
print(courses)