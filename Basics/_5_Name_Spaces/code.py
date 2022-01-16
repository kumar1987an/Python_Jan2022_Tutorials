print(dir())
print("\n")
x = 222
fruit_name = "apple"
print(dir())

# import secrets
from secrets import choice

print("\n")
print(dir())

from math import ceil as ce

print("\n")
print(dir())


def formula1(x):
    return x + 100


class Zombie:
    pass


print("\n")
print(dir())

print("\n")
print(locals())
print("\n")
print(type(locals()["x"]))
print(type(locals()["__name__"]))
print(type(Zombie))
print(type(__annotations__))
print(type(__name__))
print(type(__package__))
print(type(formula1))
print(type(fruit_name))
print(type(__loader__))
print(type(__spec__))
print(type(choice))
print(type(ce))
