class Dog:  # without initialization

    species = "Canis Familiaris"  # Class Attribute

    def dog_species(self, name, age):  # name and age is method attribute
        return f"""
        Species : {Dog.species}
        Name    : {name}
        age     : {age}"""


dog1 = Dog()  # dog is an instance
print(dog1.__class__)
print(dog1.dog_species("Tim", 4))
dog2 = Dog()
print(dog2.dog_species("Rock", 2))


class Arithmetic:  # With initialization
    def __init__(self, num1, num2) -> None:
        self.num1 = num1  # instance Attributes
        self.num2 = num2  # instance Attributes

    def __add__(self):
        return self.num1 + self.num2


print()
arith1 = Arithmetic(1, 2)
print(arith1.num1)
print(arith1.num2)
print(arith1.__add__())

arith2 = Arithmetic(8, 9)
print(arith2.__add__())
print(arith1.__add__() + arith2.__add__())


print()


class Shapes:
    def circle(radius, diameter):
        return radius ** 2, diameter * 2


shape1 = Shapes
print(shape1)
print(shape1.circle(2, 2))
