""" This is a file documentation """


def string_formatting():

    """This function provides the details of string formatting"""

    s1 = ""
    print("Empty string with double quote: ", s1)
    s2 = " g"
    print(s2)
    print(bool(" "))
    s3 = "gold"
    print(s3)
    s4 = "gold is Au"
    print(s4)
    s5 = "gold is Au\nhydrogen is h2"
    print(s5)
    s6 = r"gold is Au\n hydrogen is h2"
    print("This is raw string: ", s6)
    s7 = ""
    print("Empty string with singe quote: ", s7)
    s8 = "hi there, how's the day"
    print(s8)
    s9 = "gold is Au\n\t\thydrogen is h2"
    print(s9)
    s10 = "first line\nsecond line\nthird line"
    print(s10)
    print()
    s11 = """first line
    second line
    third line"""
    print(s11)


print(string_formatting.__doc__)
print(__doc__)

import string

print("abcdefghijklmnopqrstuvwxyz")
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.digits)

print(12345)
print("12345")

name_of_person = "xyz"
tel_number = "125-363-4936"
Address = "67, street 100 , Chicago"
print(name_of_person)
print(tel_number)
print(Address)

x = 123445 - 89j
y = str(x)
print(y)
print(type(y))

print()
# Accessing part of string

s12 = "Welcome to Python Day 4 tutorials"
print(s12)
print(s12[9])
