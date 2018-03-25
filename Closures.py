
# def outer_func():
#     msg = "hi"
#
#     def inner_func():
#         print(msg)
#
#     return inner_func
#
# my_func = outer_func()
#
# my_func()

# def outer_func(message):
#     msg = message
#
#     def inner_func():
#         print(msg)
#
#     return inner_func
#
# hi_func = outer_func("Hi")
# hello_func = outer_func("Hello")
#
# hi_func()
# hello_func()

def logger(func):
    def log_func(*args):
        print("Running {} with arguments {}".format(func, args))
        print(func(*args))
    return log_func

def add(x, y):
    return x + y

def sub(x, y):
    return  x - y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 4)
sub_logger(4, 1)