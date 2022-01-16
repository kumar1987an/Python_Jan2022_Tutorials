t1 = (
    1,
    2.0,
    4,
    5,
    5,
    5,
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
)
print(
    """
These are the methods available for tuple class under 
t1 variable, also these t1 methods would be 
the same as dir(tuple) as t1 have tuple data type"""
)
print("======================================================")
print(dir(t1))
print()
print(f"{t1.count(5) = }")
print(f"{t1.index([8, 7, 6]) = }")
