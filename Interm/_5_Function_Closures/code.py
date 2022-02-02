# def outer_function():
#     message1 = "Hi"
#     message2 = "Hello"

#     def inner_function():
#         return (message1, message2)

#     return inner_function()


# print(outer_function)

# print(inner_function())


def outer_function():
    message1 = "Hi"
    message2 = "Hello"

    def inner_function():
        return message1, message2

    return inner_function


my_func = outer_function()
print(my_func())
