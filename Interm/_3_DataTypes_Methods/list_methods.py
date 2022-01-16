# List Datatype Methods

L1 = [
    1,
    2.0,
    3 + 4j,
    2.0,
    bin(2000),
    hex(151),
    oct(26),
    [
        8,
        7,
        6,
    ],
    (100, 200),
    (100, 200),
    "apple",
    "N",
    {89, 78, 67, 45},
    dict(a=10, b=20),
]

print(
    """
These are the methods available for list class under 
L1 variable, also these L1 methods would be 
the same as dir(list) as L1 have list data type"""
)
print("======================================================")
print(dir(L1))
print()
print(f"{L1 = }")
print()
L1.append(100)
print(f"L1.append(100) = {L1}")
print()
L1.extend([1, 2, 3, 4, 5])
print(f"L1.extend(1,2,3,4,5) = {L1}")
print()
print(f"{L1.count((100, 200)) = }")
print()
print(f"{L1.index((100, 200)) = }")
print()
L1.insert(7, (300, 400))
print(f"L1.insert(7, (300, 400)) = {L1}")
print()
print(L1.pop(-5))
print(f"L1.pop(-5) = {L1}")
print()
L1.remove([8, 7, 6])
print(f"L1.remove([8, 7, 6]) = {L1}")
print()
L1.reverse()
print(f"L1.reverse() = {L1}")
print()
L1.clear()
print(f"L1.clear() = {L1}")
print()
