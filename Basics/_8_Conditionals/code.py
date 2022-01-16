x = 0
y = 5

if x < y:
    print("x < y = Yes")

if y < x:
    print("y < x = Yes")

if x:
    print("x = Yes")

if y:
    print("y = Yes")

if x or y:
    print("x or y = Yes")

if x and y:
    print("x and y = Yes")

if "eat" in "great":
    print("eat in great is Yes")

if "baz" in [
    "foo",
    "bar",
    "baaz",
    "abazg",
    "baz",
]:
    print("baz in iterable is Yes")

# %%
if "foo" in ["bar", "baz", "quix"]:
    print("Expression was true")
    print("Executing statement in this container suite")
    print("Done")
print("Post Conditional statement executed")

# %%
if "foo" in ["foo", "bar", "baz"]:
    print("Outer Condition is True")
else:
    print("Outer Condition is False")

# %%
if "foo" in ["foo", "bar", "baz"]:
    print("Outer Condition is True")

    if 10 > 20:
        print("Inner Condition 1")

    print("End of Outer condition")

print("After Outer condition")
# %%
if "foo" in ["foo", "bar", "baz"]:
    print("Outer Condition is True")

    if 10 > 20:
        print("Inner Condition 1")

    print("Between Inner Condition")

    if 10 < 20:
        print("Inner condition 2")

    print("End of Outer condition")

print("After Outer condition")

# %%
x = 20

if x > 50:
    print("(first block)")
    print("x is small")
else:
    print("(second block)")
    print("x is large")

# %%
x = 3
y = "apple".upper()
if x == 1 and y == "apple":
    print("foo")
    print("bar")
    print("baz")

elif y == "APPLE":
    print("qux")
    print("quux")

else:
    print("corge")
    print("grault")

# %%
"""
if a > b:
    m = a
else:
    m = b
"""

# %%
a = 20
b = 7
m = a if a > b else b
print(m)

# %%
x = y = 40
z = (1 + x) if x > y else (y + 2)
print(z)

# %%
x = y = 40
z = 1 + (x if x > y else y) + 2
print(z)

# %%
x = 20
s = (
    "foo"
    if (x == 1)
    else "bar"
    if (x == 2)
    else "baz"
    if (x == 3)
    else "qux"
    if (x == 4)
    else "quux"
)
print(s)
# %%
