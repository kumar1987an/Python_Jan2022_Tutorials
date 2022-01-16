import math

# Conditional statements
print(1 < 2)
print(math.sqrt(121) == 11)
print(10.0 > 10)

print("\n")

# Truthiness check

print(bool([]))
print(bool([1]))
b1 = bool([1])
print(bool({}))
print(bool({1, 2}))
print(bool(int()))
print(bool(int(89)))
print(bool(float()))
print(bool(float(67.1)))
print(bool(dict()))
print(bool(dict(a=22)))
print(bool(""))
print(bool("Apple"))
print(b1)
