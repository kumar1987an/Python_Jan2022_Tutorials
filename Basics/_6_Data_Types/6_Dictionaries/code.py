d1 = dict()  # Empty dictionary
d2 = {1: 1, 2: 2, 3: 3}
d3 = dict((("Name", "Python"), ("Age", 40)))
d4 = dict(Name="Python", Age=40, list_of_libs=["requests", "html5lib"])
print(d1)
print(d2)
print(d3)
print(d4)
print(d4["Name"])
print(d4["list_of_libs"][0])
