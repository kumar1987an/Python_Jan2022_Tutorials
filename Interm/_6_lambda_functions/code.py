from tkinter import Variable


lambda_1 = lambda x: x ** 2
print(lambda_1(20))

print((lambda x: x ** 2)(20))
print((lambda x, y, z: x + y + z)(8, 9, 10))
print((lambda x, y, z=3: x + y + z)(8, 9, 10))
print((lambda *args: sum(args))(1, 2, 3))
print((lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3))
