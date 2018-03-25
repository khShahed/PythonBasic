
"""def simple_addition(num1, num2):
    answer = num1 + num2
    print('num1 is ', num1)
    print(answer)

#simple_addition(3, 5)
simple_addition(num2=3, num1=5)"""

# def simple(num1, num2):
#     pass
#
# def simple(num1, num2=5):
#     print(num1, num2)

#simple(5)

# def basic_window(width, height, font="TNR",
#                  bgc="w", scrollbar=True):
#     print(width, height, font, bgc, scrollbar)

#basic_window(500, 350)
#basic_window(500, 350, "W")
#basic_window(500, 350, bgc="Red")
# basic_window(500, 350, scrollbar = False)

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ["Math", "Art"]
info = {'name':"John", 'age':22}

student_info(*courses, **info)
