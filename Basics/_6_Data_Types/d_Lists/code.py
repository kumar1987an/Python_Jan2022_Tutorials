L1 = []
print(L1)
print(bool(L1))


def upper_char(x):
    return x.upper()


class Testing:
    def __init__(self) -> None:
        pass


L1 = [
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
    upper_char("alpha"),  # all caps string (function)
    Testing,  # Class
    [1, 2, 3, [1, 4, 5, [78, 89, 78, [0, 0, 0, 0]]]],  # Nested List
]

print(L1)
print("List of elements in the list is ", len(L1))
print(f"L1[0] = {L1[0]}")
print(f"L1[10] = {L1[10]}")
print(f"L1[13] = {L1[13]}")
print(f"L1[13][3][3][3] = {L1[13][3][3][3]}")

L1[8] = -56 - 45j
print(f"Modified list L1 with 8 element :  {L1}")
