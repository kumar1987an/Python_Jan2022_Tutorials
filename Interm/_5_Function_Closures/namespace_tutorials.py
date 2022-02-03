# """ This tutorial is for explaining about Namespaces in Python """

# def f():
#     print("Start f()")

#     def g():
#         print("Start g()")
#         print("End g()")

#     g()

#     print("End f()")


# f()

# x = "GLOBAL"


# def f():
#     x = "ENCLOSING"

#     def g():
#         x = "LOCAL"
#         print(x)
#         print(locals())

#     g()


# f()
# print(globals())

# Global Declaration

# x = 20


# def f():
#     global x
#     x = 40
#     print(x)


# f()
# print(x)

x = 100


def f():
    x = 20

    def g():
        nonlocal x
        x = 40

    g()
    print(x)


f()
print(x)
