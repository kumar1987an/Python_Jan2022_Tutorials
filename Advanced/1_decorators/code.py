# Inner Functions
# ==================

# def outer_func(msg):
#     message = msg

#     def inner_func():
#         print(message)

#     inner_func()


# outer_func("Hello")

# Function Closures
# ==================


# def outer_func(msg):
#     message = msg

#     def inner_func(newmsg):
#         print(message + " " + newmsg)

#     return inner_func


# new_func = outer_func("Hello")
# new_func("there")


# Decorator Functions
# ==================


# Decorator 1


# def my_decorator(func):
#     def wrapper():
#         print("Something is happeneing before the function is called")
#         func()  # it is say_hello
#         print("Something is happeneing after the function is called")

#     return wrapper


# @my_decorator
# def say_hello():
#     print("Helllooo!")


# say_hello = my_decorator(say_hello)
# say_hello()


# Decorator 2


# def do_twice(func):
#     def wrapper_do_twice():
#         func()
#         func()

#     return wrapper_do_twice


# @do_twice
# def say_hello():
#     print("Hello!")


# say_hello()

# Decorator 3

from functools import wraps


# def do_twice(func):
#     @wraps(func)
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)

#     return wrapper_do_twice


# @do_twice
# def greet(name):
#     print("Creating Greeting")
#     print(f"Hi {name}")


# greet("Kumaran")


# Boilerplate template (readymade template)


# def decorated_function(func):
#     @wraps(func)
#     def wrapped_function(*args, **kwargs):
#         value = func(*args, **kwargs)
#         return value

#     return wrapped_function

# REal world examples

# import time


# def timer(func):
#     """Print the runtime of the decorated function"""

#     @wraps(func)
#     def wrapper_timer(*args, **kwargs):
#         start_time = time.perf_counter()
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         run_time = end_time - start_time
#         print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
#         return value

#     return wrapper_timer


# @timer
# def waste_some_time(num_times):
#     for _ in range(num_times):
#         sum([i ** 2 for i in range(10000)])
#     else:
#         return "Loop finished"


# print(waste_some_time(1000))
# print(waste_some_time.__name__)
# line 117 ==> wrapping  wrapper_timer to waste_some_time
# =====================================================================


from repeater import repeat


@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")


greet("Friends")
print(greet.__name__)
