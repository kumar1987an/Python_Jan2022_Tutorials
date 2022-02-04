# Syntax is lambda x: x

lambda_1 = lambda x: x ** 2
print(lambda_1(20))

print((lambda x: x ** 2)(20))
print((lambda x, y, z: x + y + z)(8, 9, 10))
print((lambda x, y, z=3: x + y + z)(8, 9, 10))
print((lambda *args: sum(args))(1, 2, 3))
print((lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3))


def normal_outer_func(x):

    y = 4

    def normal_inner_func(z):
        print(f"x = {x}, y = {y}, z = {z}")
        return x + y + z

    return normal_inner_func


for i in range(5):
    closure = normal_outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")

print()


def lambda_outer_func(x):
    y = 4
    return lambda z: f"x = {x}, y = {y}, z = {z} => output = {x + y + z}"


for i in range(5):
    closure = lambda_outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")

print()

# map()
# filer()
from functools import reduce

# reduce()

# Syntax for map(any_function, iterable), pass the map object to an iterable
# ============================================================================

print(tuple(map(lambda x: x.upper(), ["cat", "cow", "lamb"])))  # using lambda function

# output: ("COW", "LAMB")

circle_areas = [3.57666, 5.562, 6.8, 9.45, 2.22]
print(list(map(round, circle_areas)))  # round is inbuilt function


def upper_case(animal):
    return animal.upper()


print(
    list(map(upper_case, ["cat", "cow", "lamb"]))
)  # upper_case is user defined function

print()

# Syntax for filter(any_function, iterable), pass the filer object to an iterable
# ============================================================================

print(list(filter(lambda x: "o" in x, ["cow", "dog", "frog", "cat"])))  # with lambda

scores = [67, 45, 77, 89, 78, 90, 81]


def one_of_the_students(score):
    return score > 75


print(list(filter(one_of_the_students, scores)))  # with user defined function


# reduce function

print(reduce(lambda acc, x: f"{acc} - {x}", ["cat", "cow", "dog"]))

print()

# complex lambda functions


print(
    (lambda some_list: list(map(lambda n: n // 2, some_list)))(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
)

# Method 2 with normal function


def floor_divide_items(some_list):
    div_by_two = lambda n: n // 2
    return list(map(div_by_two, some_list))


print(floor_divide_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
