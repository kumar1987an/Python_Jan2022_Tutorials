# Range For Loop

# print(help(range))
print(range(0, 10, 2))

# Positive for loop
for element in range(0, 10):  # 0 - Default Start value, 1 - Default Step value
    # if element % 3 == 0:
    print(element)

print()

# Negative for loop
for element in range(-1, -10, -1):  # 0 - Default Start value, 1 - Default Step value
    print(element)

print()

# With step value
for element in range(1, 11, 2):  # 0 - Default Start value, 1 - Default Step value
    print(element)

print()
# Performing an operation 10 times
for _ in range(0, 10):
    print("Hello World")

print()
# Iterating over element in an List iterable
L1 = ["apple", "orange", "jackfruit", "pumpkin"]
for element in L1:
    if element == "jackfruit":
        break
    print(element)

print()

# tuple iterable unpacking with For loop
t1 = ("apple", "orange", "jackfruit", "pumpkin")
for element in t1:
    print(element)


print()

# dictionary iterable with For loop
d1 = dict(a=100, b=200, c=300)
for key, value in d1.items():
    print(key)
    print(value)

print()

# Set iterable with for loop
s1 = {1, 2, 3, 4, 4, 4, 4, 5}
for element in s1:
    print(element)

print()

# Strings with for loop
string1 = "apple"
for char in string1:
    print(char)

print()

L2 = "apple orange jackfruit grapes".split()
print(L2)

# While Loops

n = 5
while n > 0:
    print(n)
    n = n - 1

print("==================")

# Container based while loop

a = "foo bar baz bliss".split()
while a:
    print(a.pop(-1))

print("==================")

# while loop with break statement
n = 5
while n > 0:
    if n == 2:
        break
    print(n)
    n = n - 1
else:
    print("loop ended")

# while loop with break and continue statement

print("==================")
n = 10
while n > 0:
    n = n - 1
    if n == 5:
        continue
    if n == 2:
        break
    print(n)
