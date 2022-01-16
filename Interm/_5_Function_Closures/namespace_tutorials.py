# def f():

#     print("Start f()")

#     def g():
#         print("Start g()")
#         print("End g()")

#     g()

#     print("End f()")


# f()

# =================================================

# x = "global"


# def f():
#     x = "enclosing"
#     print(f"locals() of f = {locals()}")

#     def g():
#         x = "local"
#         print(f"locals() of g = {locals()}")

#     g()


# f()

# =================================================

# x = 20


# def f():
#     global x
#     x = 40
#     print(f"f() = {x = }")


# f()
# print(f"global scope variable = {x = }")

# =================================================

x = 100


def f():
    x = 30
    print(type(x))

    def g():
        nonlocal x
        x = 40

    g()
    print(x)


f()
print(x)


print(globals())
