# Inner Functions
# ===============


# def outer_func(msg):
#     message = msg

#     def inner_func():
#         print(message)

#     inner_func()


# outer_func("Hello")

# Function closures
# =================


# def outer_func(msg):
#     message = msg

#     def inner_func(newmsg):
#         print(message + " " + newmsg)

#     return inner_func


# new_func = outer_func("Hello")
# new_func("Hi")


# Decorator function
# =================

# Decorator 1


def my_decorator(func):  # for func argument say_hello function being used
    def wrapper():
        print("Something is happening before the function is called")
        print(func())  # say_hello function got executed
        print("Something happened after the function is called")
        output = func()
        print(output.upper())

    return wrapper


@my_decorator
def say_hello():
    return "Helllooo"


# Method1 of executing decorator
# new_say_hello = my_decorator(say_hello)
# new_say_hello()

say_hello()

print()


# Decorator 2


def do_twice(func):
    def wrapper_do_twice():
        func()
        func()

    return wrapper_do_twice


@do_twice
def say_hello1():
    print("Hello")


say_hello1()

print()

# ===========================================================================

from functools import wraps
from textwrap import wrap


def greet_decorator(func):
    @wraps(func)
    def wrapper_greet(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_greet


@greet_decorator
def greet(name):
    print("Creating Greeting")
    print(f"Hi {name}")


greet("Kumaran")
print(greet.__name__)

print()

# ==============================================================================

from repeater import repeat


@repeat(num_times=10)
def greeting(name):
    print(f"Hello {name}")


greeting("DXC")

# ==============================================================================

# Boilerplate template (readmade template)


def decorated_function(func):
    @wraps(func)
    def wrapped_function(*args, **kwargs):
        value = func(*args, **kwargs)
        return value

    return wrapped_function


@decorated_function
def greeting(give_range):
    print([i for i in range(give_range)])


greeting(20)
