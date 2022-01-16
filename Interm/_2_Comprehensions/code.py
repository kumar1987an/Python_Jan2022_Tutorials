# for loop - Actual method

L1 = []
for i in range(5):
    L1.append(i)

print("Using Traditional Method", L1)

# List comprehension

L1 = [i for i in range(5)]
print("using list comprehension", L1)

# [element for element in <iterable> <if condition>]

print()
L1 = [i for i in range(1000) if i % 10 == 0]
print(L1)

# Set comprehension
print()
set1 = {i for i in range(1000) if i % 10 == 0}
print(set1)

# # Dictionary comprehension
print()
d1 = {key: value for key, value in zip("a b c".split(), [100, 200, 300])}
print(d1)
