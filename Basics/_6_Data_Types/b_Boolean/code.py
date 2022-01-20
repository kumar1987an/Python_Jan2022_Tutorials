x = 7
y = 49
print(x > y)
print(x < y)
print(x == y)
print(x != y)
print(x > y or x < y)
print(x < y and x == y)
print(x not in [1, 2, 3, 4, 7])
print()
# Truthiness

print(f"bool('') = {bool('')}")
print(f"bool('Python@123') = {bool('Python@123')}")

print(f"bool([]) = {bool([])}")
print(f"bool([1, 67, 78]) = {bool([1, 67, 78])}")

print(f"bool(tuple()) = {bool(tuple())}")
print(f"bool((1, 67, 78)) = {bool((1, 67, 78))}")

print(f"bool(set()) = {bool(set())}")
print(f"bool({1, 2, 3, 3, 4, 5}) = {bool(set((1, 2, 3, 3, 4, 5)))}")

print(f"bool(dict()) = {bool(dict())}")
print(f"bool(dict(a=2)) = {bool(dict(a=2))}")

print(f"bool(float()) = {bool(float())}")
print(f"bool(float(78)) = {bool(float(78))}")

print(f"bool(int()) = {bool(int())}")
print(f"bool(int(78)) = {bool(int(78))}")
