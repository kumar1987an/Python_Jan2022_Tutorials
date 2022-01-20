t1 = tuple()
print(t1)
print(bool(t1))
t1 = tuple(
    (
        2,  # Integer number
        3.076,  # Floating point number
        78,
        (100, 78, 1),  # Tuple
        {1, 2, 3, 4, 5, 3},  # Set
        "omlet",  # String
        "G",
        dict(a=7, c=56, b=3),  # Dictionary
        -56 + 45j,  # Complex
        bin(56),  # Binary number
        hex(90),  # Hexa decimal number
        [1, 2, 3, [1, 4, 5, [78, 89, 78, [0, 0, 0, 0]]]],  # Nested List
    )
)

t2 = (
    2,
    3.076,
    78,
    (100, 78, 1),
    {1, 2, 3, 4, 5, 3},
    "omlet",
    "G",
    dict(a=7, c=56, b=3),
    -56 + 45j,
    bin(56),
    hex(90),
    [1, 2, 3, [1, 4, 5, [78, 89, 78, [0, 0, 0, 0]]]],
)

print(t1)
print(t2)
print(t1)
print("List of elements in the list is ", len(t1))
print(f"t1[0] = {t1[0]}")
print(f"t1[10] = {t1[10]}")
print(f"t1[11] = {t1[11]}")
print(f"t1[11][3][3][1] = {t1[11][3][3][1]}")


# t1[0] = 100
# print(t1)
