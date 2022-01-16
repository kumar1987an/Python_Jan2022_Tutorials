#  Set Methods
print(
    """
These are the methods available for set class under 
a, b, c, d variables, also these set (a,b,c,d) methods would be 
the same as dir(set) as above variables have dict data type"""
)
print("======================================================")
a = {1, 2, 3, 4, 5}
b = {2, 3, 4, 5, 6}
c = {3, 4, 5, 6, 7}
d = {4, 5, 6, 7, 8}
print(dir(a))
print()
print(len(d))
print()
print(len(set()))
print({[1, 2, 2, 3, 4, 5]})
print({{"a": 1, "b": 2}})
print(set(tuple((1, 2, 3, 4))))
print(type({}))
x = {'foo', 'bar', 'baz'}
for element in x:
    print(element)
print({("apple", "apple")})
print(set("apple"))
# print(x[-1])
print()
print(f"{a.union(b) = }")  # union of
print(f"{a.union(b, c, d) = }")  # union of
print(f"{a.union([8, 9, 10]) = }")
print(f"{a.union(dict(apple='red')) = }")
print(f"same of a.union(b) {a | b = }")
print(f"same of a.union(b, c, d) {a | b | c | d = }")
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
print(x1 | x2)
print(x1.union(x2))
print(x1.union(('baz', 'qux', 'quux')))
# print(x1 | ('baz', 'qux', 'quux'))
print()

print(f"{a.intersection(b) = }")  # intersection of
print(f"{a.intersection(b, c, d) = }")  # intersection of
print(f"same of a.intersection(b) {a & b = }")
print(f"same of a.intersection(b, c, d) {a & b & c & d = }")

print()
print("Difference of multiple sets is the set of only the elements"
      "that exist in the first set but not in any of the rest")
print(f"{a.difference(b) = }")  # difference of
print(f"{a.difference(b, c, d) = }")  # difference of
print(f"same of a.difference(b) {a - b = }")
print(f"same of a.difference(b, c, d) {a - b - c - d = }")
print(f"{b.difference(a) = }")  # difference of
print(f"{b.difference(a, c, d) = }")  # difference of
print(f"same of a.difference(b) {b - a = }")
print(f"same of a.difference(b, c, d) {b - a - c - d = }")

a = {1, 2, 3, 4, 5}
b = {10, 2, 3, 4, 50}
c = {1, 50, 100}
print()
print("Symmetric difference of multiple sets is the set of only"
      "the elements that exist in a single set, but not in multiple")
print(f"{a.symmetric_difference(b) = }")  # symmetric_difference of
print(f"{a.symmetric_difference(b) = }")  # symmetric_difference of
print(f"same of a.symmetric_difference(b) {a ^ b = }")
print(f"same of a.symmetric_difference(b, c, d) {a ^ b ^ c = }")

print()
"""
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
"""

print("Determines whether or not two sets have any elements in common")
print(x1.isdisjoint(x2))
print(x2 - {'baz'})
print(x1.isdisjoint(x2 - {'baz'}))

x1 = {1, 3, 5}
x2 = {2, 4, 6}
print(x1.isdisjoint(x2))
print(x1 & x2)
#  Only works with one argument (comparing two sets)
#  Argument needs to be iterable
#  No operator used

print()
print("A set is considered as a subset of another set if "
      "every element of the first set is in the second set")
x1 = {"foo", "bar"}
x2 = {"foo", "bar", "baz"}
print(f"{x1.issubset(x2) = }")  # checking for subset
print(f"{x1.issubset(x1) = }")
# Argument need to be an iterable
a = {1}
b = {1, 2}
c = {1, 2, 3}
d = {1, 2, 4}
print(f"{a <= b = }")
print(f"{b <= c = }")
print(f"{a <= b <= d = }")
print(f"{a <= c <= d = }")
# Operands need to be sets
# Works with multiple sets and compares if each set is a subset of all the rest
# of the sets


print()
print("A set is considered as a superset of another set if "
      "first set contains every element of the second set")
x1 = {"foo", "bar", "baz"}
x2 = {"foo", "bar"}
print(f"{x1.issuperset(x2) = }")  # checking for subset
print(f"{x1.issuperset(x1) = }")
# Argument need to be an iterable
a = {1}
b = {1, 2}
c = {1, 2, 3}
d = {1, 2, 4}
print(f"{b >= a = }")
print(f"{c >= b = }")
print(f"{d >= b >= a = }")
print(f"{d >= c >= a = }")
# Operands need to be sets
# Works with multiple sets and compares if each set is a supersubset of all the rest
# of the sets

print()
x1 = {"foo", "bar", "baz"}
x1.add("slate")
print(f"set {x1 = }")
# x1.add(["goat"])

print()
x1.remove("baz")
print(f"set {x1 = }")
# x1.remove("chalk")

print()
x1.discard("bar")
print(f"set {x1 = }")
x1.discard("chalk")

print()
d = {100, 673, 567, 1000, 2, 0}
d.pop()
print(f"set d is now after pop method {d = }")
d.pop()
print(f"set d is now after pop method {d = }")
d.pop()
print(f"set d is now after pop method {d = }")
d.pop()
print(f"set d is now after pop method {d = }")
print(d.pop())
print(f"set d is now after pop method {d = }")
