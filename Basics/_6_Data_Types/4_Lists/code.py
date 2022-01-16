L1 = []  # Empty list


def f1(x):
    return x ** x


class Test:
    def __init__(self) -> None:
        pass


L2 = [
    1,
    2.0,
    3 + 4j,
    bin(2000),
    hex(151),
    oct(26),
    f1(2),
    Test.__name__,
    [
        8,
        7,
        6,
    ],
    (100, 200),
    "apple",
    "N",
    {89, 78, 67, 45},
    dict(a=10, b=20),
]
print(L2)
print()
for index, element in enumerate(L2):
    print(str(index) + ": " + str(element))

print()

L2[8] = "alpha"
for index, element in enumerate(L2):
    print(str(index) + ": " + str(element))

print(L2)

L3 = list(
    (
        1,
        2,
        3,
        4,
    )
)
print()
print(L3)
