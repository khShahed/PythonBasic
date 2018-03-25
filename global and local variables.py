"""
    LEGB
    Local, Enclosing, Global, Built-in
"""


'''x = 6

def example():
    print(x) #no error
    print(x+6) #no error
    x += 1 #error

example()'''

'''x = 6

def example():
    global x
    print(x) #no error
    print(x+6) #no error
    x += 1 # no error
    print(x)

def example2():
    x += 2 #error
    print(x)

example()
example2()'''

'''x = 6

def example():
    global x
    print(x) #no error
    print(x+6) #no error
    x += 1 # no error
    print(x)

def example2():
    global x
    x += 2 # no error
    print(x)

example()
example2()
print(x) #9'''
#
# x = 6
#
# def example():
#     globalx = x
#     print(globalx)
#     globalx += 5
#     print(globalx)
#     return globalx
#
# x = example()
# print(x)
    
# x = "global x"
#
# def example():
#     x = "local x"
#     print(x)
# example()
# print(x)

# x = "global x"
#
# def example():
#     global x
#     x = "local x"
#     print(x)
# example()
# print(x)

# x = "global x"
#
# def outer():
#     x = "outer x"
#
#     def inner():
#         x = "Inner x"
#         print(x)
#
#     inner()
#     print(x)
#
# outer()
# print(x)

x = "global x"

def outer():
    x = "outer x"

    def inner():
        nonlocal x
        x = "Inner x"
        print(x)

    inner()
    print(x)

outer()
print(x)