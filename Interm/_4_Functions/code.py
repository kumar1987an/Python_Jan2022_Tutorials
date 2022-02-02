# Code


def greeting():
    print("Hellloooooo World!" + " Happy New Year Everybody")


# greeting()


def return_greeting():
    print("Thank you")
    return "Hellloooooo World!" + " Wish you the same", "Enjoy the life"


# return_greeting()

return_greet1, return_greet2 = return_greeting()
print(return_greet1)
print(return_greet2)


# Tuple unpacking
x, y = 20, 30  # This is applied on line number 18
print(x)
print(y)

print()


def power_of_two(x: int) -> int:  # This is called type hinting
    """This function is used to get the power of 2 with the given value x"""
    return pow(x, 2)


print(power_of_two(4536272838392973))


print()


def name_of_a_person(fname: str, lname: str) -> str:
    return (
        lname.title() + " " + fname.title(),
        f"length of lname: {len(lname)}, length of fname: {len(fname)}",
    )


# print(name_of_a_person("kumaran", "ramalingam"))
name_of_person, len_of_name = name_of_a_person("kumaran", "ramalingam")
print(name_of_person)
print(len_of_name)

print()
# Default Argument(s) function

from math import pi


def area_of_circle(radius: int = 10) -> float:  # (radius = 10 is default argument)
    return pi * (radius ** 2)


print(f"Area of circle: {area_of_circle(100) = }")
print(f"Area of circle: {area_of_circle()}")

print()
# Positional Argument(s) function


def normal_arg_functions(x: int, y: int, z: str) -> tuple:
    return x ** 2, y / 400, len(z)


print(normal_arg_functions(7, 700, "bricks"))


def positional_arg_functions(*args):
    # return args
    for count in args:
        print(count)


positional_arg_functions(7, 700, "bricks")

# Keyword Argument(s) function

print()


def keyword_arg_function(**kwargs):
    # return args
    for key, value in kwargs.items():
        print(key, value)


keyword_arg_function(a=0, b=1, c=2)

# Combining both positional and keyword args

print()


def all_together(city="Italy", *args, **kwargs):
    print(f"City: {city}")
    print(f"Cordinates: {args}")
    print(f"Bus route number: {kwargs}")


bus_routes = dict(bus_route1=77, bus_route2=101)
# all_together("10N", "88",**bus_routes)
all_together("Italy", "10N", "88", bus_route1=77, bus_route2=101)
