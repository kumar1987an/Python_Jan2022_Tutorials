print()
# Functions without arguments
def greet():
    print("Helloooooo World!!!" + " Happy New Year")

greet()


# Method 1

def power_of_two(x): # Function definition
    """ This function is used to get the power of 2 with the value x """
    print(x ** 2)

# Method 2
def power_of_three(x):  # Function definition
    """ This function is used to get the power of 2 with the value x """
    return x ** 3

# Function call
power_of_two(56373854683363)
cubic_power = power_of_three(56373854683363)
print(cubic_power)

def name_of_the_persion(fname, lname):
    return lname.upper(), fname.upper()

print(name_of_the_persion("kumaran", "ramalingam"))
last_name, first_name = name_of_the_persion("kumaran", "ramalingam")
print(last_name)
print(first_name)

print("=====================")

# Default Arguments Function

from math import pi
def area_of_circle(radius=10): # radius = 10 is the default argument
    return pi * (radius ** 2)

print(area_of_circle(67))
print(area_of_circle())

print(pi)
def circumference_of_circle(radius=2):
    return 2 * pi * radius

print(circumference_of_circle(10))
def price_of_100_stickers():
    return circumference_of_circle(10) * 100

print(price_of_100_stickers())

# Positional Arguments Function

def normal_arguments_function(x, y, z, a, b, c):
    return x**2, y/200, z.upper(), a, b, c

print(f"{normal_arguments_function(10, 20, 'thirty', 40, 50, 60) = }")

def positional_arguments_function(*args):  # *args is for positional arguments
    for count in range(len(args)):
        print(args[count])
    num_of_elements_in_function = len(args)

positional_arguments_function(10, 20, 'thirty', 40, 50, 60)

# Keyword Arguments Function

def keyword_arguments_function(**kwargs):
    data = kwargs
    return data.keys()

print(keyword_arguments_function(name="Kumaran", exp=12))

# Mix of all arguments

def default_positional_keyword_function(city="xyz", *args, **kwargs):
    print(city)
    print(args, len(args))
    print(kwargs)

d1 = dict(a=10, b=1)
default_positional_keyword_function(20, 10, **d1)

print(tuple([1, 2, 3, 4]))