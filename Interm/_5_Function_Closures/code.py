# Inner Function


from math import perm


def outer_function():
    message1 = "Hi"
    message2 = "Hello"

    def inner_function():
        print(message1, message2)

    inner_function()


outer_function()


print()


def factorial(number):  # outer or enclosing function
    # Validate input

    if not isinstance(number, int):
        raise TypeError("Sorry, 'number' variable must be an integer")

    if number < 0:
        raise ValueError("Sorry, 'number' must be zero or positive")

    # Calculate the factorial of number
    def inner_factorial(number):  # inner or enclosed function
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)

    return inner_factorial(number)


print(factorial(5))


# Closure Functions


def outer_func(msg):

    message = msg

    def inner_func():
        print(message)

    return inner_func


hello_func = outer_func("Hello")
print(hello_func.__name__)
print(hello_func)

# =====================================


def generate_power(exponent):
    def power(base):
        return base ** exponent

    return power


raise_two = generate_power(2)
raise_three = generate_power(3)
raise_four = generate_power(4)

print(raise_two(30))
print(raise_three(100))
print(raise_four(100))
print(raise_two.__name__)


def has_permission(page):
    def permission(username):
        if username.lower() == "admin":
            return f"'{username}' has access to {page}."
        else:
            return f"'{username}' have no access to {page}."

    return permission


check_admin_page_permission = has_permission("Admin Page")
print(check_admin_page_permission("admin"))
print(check_admin_page_permission("John"))
