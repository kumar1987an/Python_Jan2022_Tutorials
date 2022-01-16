# String Datatype methods

string_1 = "foo baz bar jazz bazz"
string_2 = "-16273537830"
string_3 = "     {}     ".format(string_1)
string_4 = "{}.6789".format(string_2)
print(
    """
These are the methods available for string class under 
string_1 variable, also these string_1 methods would be 
the same as dir(str) as string_1 have str data type"""
)
print("======================================================")
print(dir(string_1))
print()
print(f"{string_1.upper() = }")
print(f"{string_1.lower() = }")
print(f"{string_1.title() = }")
print(f"{string_1.capitalize() = }")
print(f"{string_1.startswith('foo ba') = }")
print(f"{string_1.endswith('az') = }")
print(f"{string_1.count('ba') = }")
print(f"{string_1 + ' {}'.format('baaz') = }")
print(f"{string_1.encode() = }")
print(f"{string_1.split() = }")
print(f"{string_3.strip() = }")
print(f"{string_1.isalpha() = }")
print(f"{string_2.isdigit() = }")
print(f"{string_3.isspace() = }")
print(f"{string_4.isdecimal() = }")
print(f"{string_1.index('jazz') = }")
print(f"{string_1.find('bar') = }")
print(f"{string_1.replace('foo', 'zoo') = }")
print(f"{string_1.partition('bar') = }")
