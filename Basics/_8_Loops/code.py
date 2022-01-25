# For Loops

print(range(0, 10))

print("=" * 15)

for value in range(5):  # start value by default 0, stop value is 5, step value is 1
    print(value)

print("=" * 15)

for value in range(2, 5):  # start = 2, stop = 5, step = 1
    print(value)

print("=" * 15)

for value in range(1, 12, 3):  # start = 1, stop = 12, step = 3
    print(value)

print("=" * 15)

for value in range(-1, -10, -1):  # start = -1, stop = -1, step = -1
    print(value)

print("=" * 15)

for _ in range(5):
    print("Hello World")

print(_)

print("=" * 15)

# List of Iterables
# list
# set
# dictionary
# tuple
# string

# Iterating over an List iterable
L1 = ["apple", "orange", "pumpkin", "jackfruit"]
print(L1)

for element in L1:
    print(element)

print()

for element in L1:
    if element == "pumpkin":
        break
    print(element)

print()

for element in L1:
    print(element)
    if element == "pumpkin":
        break

print("=" * 15)

# Iterating over an tuple  iterable
t1 = tuple(L1)  # this is equal to t1 = ("apple", "orange", "pumpkin", "jackfruit")
print(t1)


for element in t1:
    print(element)

print()

for element in t1:
    if element == "pumpkin":
        break
    print(element)

print()

for element in t1:
    print(element)
    if element == "pumpkin":
        break

print("=" * 15)

# Iterating with an Dictionary Iterable

d1 = dict(emp_id=56788, emp_name="Bob", emp_joblevel=5)
print(d1)

print()

for element in d1:
    print(element)

print()

for key, value in d1.items():
    print(f"{key} = {value}")

print()

print(d1.items())  # pair of key and value of d1
print(d1.keys())  # it has only keys
print(d1.values())  # it has only values

print()

for key in d1.keys():
    print(key)

print()

for value in d1.values():
    print(value)

print("=" * 15)
# Iterating with Set
set1 = set(L1)  # this is equal to set1 = ("apple", "orange", "pumpkin", "jackfruit")
print(set1)

for element in set1:
    print(element)

print()

for element in set1:
    if element == "pumpkin":
        break
    print(element)

print()

for element in set1:
    print(element)
    if element == "pumpkin":
        break

print("=" * 15)

# Iterating over a string

string1 = "Melon = Vit-C"
for char in string1:
    print(char)

print("=" * 15)

# While Loops

# while loops will run untill condition gets false

n = 5
while n > 0:
    print(n)
    n = n - 1

print()

string2 = "bar baz baaz bliss".split()
print(string2)

# Iterable based while loop
while string2:
    print(string2.pop(0))

print(string2)

print()

# while loop with break statement

n = 5
while n > 0:
    if n == 2:
        break
    else:
        print(n)
        n = n - 1
else:
    print("Loop Ended")

print()
# while loop with continue statement

n = 15
while n > 0:
    print(n)
    n = n - 1
    if n == 7:
        continue
    if n == 2:
        break
