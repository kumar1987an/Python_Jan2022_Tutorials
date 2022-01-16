# Arithmetic Operators

import builtins


x = 15
y = 2

print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)
print("x // y =", x // y)
print("x % y =", x % y)
print("x ** y =", x ** y)

print()
print("divmod(x, y) =", divmod(x, y))

print()
import operator as op

print("op.add(x, y) =", op.add(x, y))
print("op.sub(x, y) =", op.sub(x, y))
print("op.mul(x, y) =", op.mul(x, y))
print("op.truediv(x, y) =", op.truediv(x, y))
print("op.floordiv(x, y) =", op.floordiv(x, y))
print("op.mod(x, y) =", op.mod(x, y))
print("op.pow(x, y) =", op.pow(x, y))


# Comparison Operators
print()

x = 200
y = 214

print("x > y =", x > y)
print("x < y =", x < y)
print("x == y =", x == y)
print("x != y =", x != y)
print("x >= y =", x >= y)
print("x <= y =", x <= y)

print()
# Logical Operators

x = False
y = True

print("x and y is", x and y)
print("x or y is", x or y)
print("not x is", not x)
print("not y is", not y)

if 10 > 2 and (x or y):
    print(True)

if 10 < 2 and (x or y):
    print(True)
else:
    print(False)

print()


# Assignment Operators
x = 5
# x = x + 1
x += 1
print(x)

x = 5
x -= 1
# x = x - 1
print(x)

x = 5
x *= 5
# x = x * 5
print(x)

x = 5
x /= 5
# x = x / 5
print(x)

x = 5
x %= 2
# x = x % 2
print(x)

x = 5
x //= 2
# x = x // 2
print(x)

x = 5
x **= 5
# x = x ** 5
print(x)


print()

# Bitwise Operator

x = 10
y = 4

print(bin(x))
print(bin(y))

# 0000 1010
# 0000 0100
# 0000 1110
# & = 0
# | =

print("x & y =", x & y)
print("x | y =", x | y)
print("~x =", ~x)
print("x ^ y =", x ^ y)


print()
# Identity Operators

x = 87348792
y = 87348792
z = x

print(x)
print(y)
print(z)
print(id(x))
print(id(y))
print(id(z))
print(x is y)
print(x is z)


x1 = [1, 2, 3]
y1 = [1, 2, 3]
print(x1, y1)
print(id(x1))
print(id(y1))
print(x1 is y1)

print(type(id(x1)))


print()
a = 4
b = 2 + 2
print(id(a))
print(id(b))

print()
y1 = "apple"
y2 = "apple"
print(id(y1))
print(id(y2))

print()
b1 = {1, 2, 3}
b2 = {1, 2, 3}
print(id(b1))
print(id(b2))

print()
x3 = y3 = list((1, 2, 3))
print(id(x3))
print(id(y3))
