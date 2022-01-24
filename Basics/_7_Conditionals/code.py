x = 0
y = 20

print(x < y)

""" 
if <condition>:
    <execute something>
    if <condition>:
        <execute something>

elif <condition>:
    <execute something>

else:
    <execute something>
"""

if x < y:
    print("x is less than y")

if y < x:
    print("y is less than x")

if y:
    print(y)

if x:
    print(x)

if "eat" in "great":  # Member checking
    print("Yes 'eat' is there in 'great'")

if "baz" in ["foo", "bar", "baz"]:
    print("baz in iterable")

# =================================================

if "foo" in ["bar", "baz", "quix"]:
    print("Expression was true")
    print("Executing statment in this code block")
    print("Done")

print("Post Conditional execution")

print("=" * 10)

if "foo" in ["foo", "bar", "baz", "bar"]:
    print("Outer Condition is ", True)
    if 10 > 20:
        print("Inner condition")

else:
    print("Outer Condition is ", False)

print("=" * 10)


if "foo" in ["foo", "bar", "baz", "bar"]:
    print("Outer Condition is ", True)

    if 10 > 20:
        print("Inner Condition 1")

    print("Between Inner Condition 1")

    if 10 < 20:
        print("Inner Condition 2")

    print("Between Inner Condition 2")

else:
    print("Outer Condition is ", False)
print("End of If Else Block")

print("=" * 10)

x = 3
y = "apple".upper()

if x == 1 and y == "apple":
    print("foo")
    print("bar")
    print("baz")
elif y == "APPLES":
    print("qux")
    print("quux")
else:
    print("corge")
    print("something")


# Logic gates

# print(True or False)
# print(True or True)
# print(False or True)
# print(True and True)
# print(True and False)
# print(False and False)
