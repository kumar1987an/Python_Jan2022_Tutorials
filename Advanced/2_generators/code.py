L1 = "apple orange jackfruit soda".split()  # List
t1 = (7, 8, 9, 10, 11, 12, 13)  # Tuple
s1 = {87, "apple", 3 + 4j}  # Set
d1 = dict(a=77, b=444, c="Goa")  # Dictionary

for value in t1:
    print(value)

print()

for value in L1:
    print(value)

print()

for value in s1:
    print(value)

print()

for key, value in d1.items():
    print(key, value)


print()

print([value.upper() for value in L1])  # List comprehension
print({value for value in s1})  # Set Comprehension
print({key: value for key, value in d1.items()})  # Dictionary Comprehension
print((value for value in t1))  # Python Generators


print()

generator = (i ** 2 for i in range(10))
print(next(generator))
print(next(generator))
print(next(generator))


print()
for _ in range(5):
    print(next(generator))

print()

print(next(generator))
print(next(generator))
# print(next(generator))

print()


def normal_function():
    for x in range(5):
        return "Hello", len("Hello")


print(normal_function())
print(normal_function())


def generator_function():
    for x in range(5):
        yield "Hello", len("Hello")


print(generator_function())
print(next(generator_function()))
print(next(generator_function()))
print()
for i in range(3):
    print(next(generator_function()))


print()


def multi_yield():
    yield_str = "This will print the first string"
    yield yield_str
    yield_str = "This will print the second string"
    yield yield_str


multi_object = multi_yield()
print(next(multi_object))
print(next(multi_object))

print()


def return_check():
    return 55
    return 56


print(return_check())


def fib(a=0, b=1):
    """Generator that yields Fibonacci Numbers, a and b are the seed values"""

    while True:
        yield a
        a, b = b, a + b


print()

f = fib()
print([next(f) for i in range(100)])


# a = 0
# b = 1

# 0

# a = 1, b = 1

# 1


# a = 1, b = 2

# 1

# a = 2, b = 3

# 2

# a = 3, b = 5

# 3

# a = 5, b = 8

# 5

# a = 8, b = 13

# 8

# a = 13, b = 21

# 13

# a = 21, b = 34
