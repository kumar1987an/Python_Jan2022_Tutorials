# Inner function

# def outer_function():
#     message1 = "Hi"
#     message2 = "Hello"

#     def inner_function():
#         return (message1, message2)

#     return inner_function()


# print(outer_function())

# print(inner_function())

# Closures

# def outer_function():
#     message1 = "Hi"
#     message2 = "Hello"

#     def inner_function():
#         return message1, message2

#     return inner_function


# my_func = outer_function()
# print(my_func())

# Example for Closure


def generate_power(exponent):
    def power(base):

        return base ** exponent

    return power


raise_two = generate_power(2)
raise_three = generate_power(3)
raise_four = generate_power(4)

print(raise_two(30))
print(raise_three(100))
print(raise_four(70))


# def outer_func(msg):
#     message = msg

#     def inner_func():
#         print(message)

#     return inner_func


# hi_func = outer_func("Hi")
# hi_func()

# hello_func = outer_func("Hello")
# hello_func()
