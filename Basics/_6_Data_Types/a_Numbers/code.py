# Numbers Data Type

int_number = 67
float_number = 56.33334
complex_number = -77+10j
binary_number = b"1101"
exponention_number = 2E-8

print(int_number)
print(float_number)
print(complex_number)
print(binary_number)
print(exponention_number)

print(type(int_number))
print(type(float_number))
print(type(complex_number))
print(type(binary_number))

x = 7
y = 26.67

print("Addition of two numbers: ", x + y)
print("Sub of two numbers: ", x - y)
print("Multiply of two numbers: ", x * y)
print("Division of two numbers 13 and 2: ", y / x)
print("Floor Division of two numbers 13 and 2: ", y // x)
print("Modulo of two numbers 13 and 2: ", y % x)
print("x to the power of y: ", x ** y)

z = 7 + 33 - 2 * ((2e-2 ** 2) + 2000) / 9
print(z)

print(2e-8 ** 2)

import math

# print(help(math))
print(dir(math))
print("Square root of 22 is " , math.sqrt(22))
print("tan theta of 3 is ", math.tan(3))
print("pi value is ", math.pi)
print("tau value is ", math.tau)
print("tan hypotenuse is ", math.tanh(7))
print("7 to the power of 2 is ", math.pow(7, 2))
print("factorial of 6 is ", math.factorial(6))
print("Euclidean distance of two numbers", math.dist([10, 2, 13], [1, 2, 2]))

import cmath

print(dir(cmath))