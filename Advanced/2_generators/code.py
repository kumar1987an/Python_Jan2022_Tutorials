L1 = "apple orange jackfruit soda".split()
t1 = 7, 8, 9, 10, 11, 12
s1 = {87, "apple", 3 + 4j}
d1 = dict(a=67, b=700, c="Goa")


for value in L1:
    print(value)

for value in t1:
    print(value)

for value in s1:
    print(value)

for key, value in d1.items():
    print(key, value)

print([value for value in L1])
print({value for value in s1})
print({key: value for key, value in d1.items()})
print(value for value in t1)

print()
generator = (i ** 2 for i in range(20))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

for value in range(10):
    print(next(generator))


print()


def normal_function():
    for x in range(10):
        return x ** 2


print(normal_function())
print()
print(normal_function())


def generator_function():
    for x in range(10):
        yield x ** 2


print(generator_function())
g1 = generator_function()
for x in range(6):
    print(next(g1))


def multi_yield():
    yield_str = "This will print the first string"
    yield yield_str
    yield_str = "This will print the second string"
    yield yield_str


print()
multi_obj = multi_yield()
print(next(multi_obj))
print(next(multi_obj))
# print(next(multi_obj))


def fib(a=0, b=1):
    """Generator that yields Fibo numbers. a and b are the seed values"""

    while True:
        yield a
        a, b = b, a + b


print()
f = fib()
for _ in range(10):
    print(next(f))
# 0, 1, 1, 2, 3, 5, 8 ,13, 21, 34
