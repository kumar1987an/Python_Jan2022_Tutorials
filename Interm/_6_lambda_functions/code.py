exec1 = lambda x: x + 200
print(exec1(7))

print((lambda x, y, z: x + y + z)(8, 9, 10))
print((lambda x, y, z=3: x + y + z)(8, 9, z=10))
exec2 = lambda x, y, z=3: x + y + z
print(exec2(8, z=100, y=9))
print((lambda *args: sum(args))(1, 2, 3))
print((lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3))
print((lambda x, y=0, z=0: x + y + z)(1, y=2, z=3))


def normal_outer_func(x):
    y = 4

    def normal_inner_func(z):
        print(f"x = {x}, y = {y}, z = {z}")
        return x + y + z

    return normal_inner_func


print()

# closure = outer_func(3)
# print(closure(2))

for i in range(3):
    closure = normal_outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")

print()


def lambda_outer_func(x):
    y = 4
    return lambda z: f"x = {x}, y = {y}, z = {z} => output = {x+y+z}"


for i in range(3):
    closure = lambda_outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")

### Lambda functional programming style

# map()
# filter()
from functools import reduce

# reduce()

print()
print(f'{tuple(map(lambda x: x.upper(), ["cat", "cow", "lamb"])) = }')
print(f'{list(filter(lambda x: "o" in x, ["cat", "dog", "cow"])) = }')
print(f'{reduce(lambda acc, x: f"{acc} | {x}", ["cat", "dog", "cow"]) = }')

print()
# Complex lambda functions
print(
    (lambda some_list: list(map(lambda n: n // 2, some_list)))(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
)

# Method 2 to solve the above complexity


def div_items(some_list):
    div_by_two = lambda n: n // 2
    return list(map(div_by_two, some_list))


print(div_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print()
ids = ["id1", "id30", "id2", "id22", "id100"]
print(sorted(ids))  # Lexicographic sort

print(sorted(ids, key=lambda x: int(x[2:]), reverse=True))
