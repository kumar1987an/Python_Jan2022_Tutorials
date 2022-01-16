""" Explanation about class construct """


class Dog1:
    """Dog1 class"""

    species = "Canis Familiaris"  # Class Attribute

    def __init__(self, name, age) -> None:
        self.name = name  # Instance Attributes
        self.age = age  # Instance Attributes

    def dog_name_age1(self):
        return f"Name of the dog is {self.name} and age is {self.age}"

    def dog_name_age2(self):
        return f"Name of the dog is {self.name} and age is {self.age}"

    def dog_name_age3(self):
        return f"Name of the dog is {self.name} and age is {self.age}"

    @staticmethod
    def dog_name_age4(name, age):
        return f"Name of the dog is {name} and age is {age}"


dog1_1 = Dog1("puppy", 2)
dog1_2 = Dog1("Pomrenian", 2)
print(
    f"Dog name {dog1_1.name} and age is {dog1_1.age} with species name {dog1_1.species}"
)
print(
    f"Dog name {dog1_2.name} and age is {dog1_2.age} with species name {dog1_2.species}"
)
print(f"Output of {dog1_1.dog_name_age1.__name__} : {dog1_1.dog_name_age1()}")
print(f"Output of {dog1_2.dog_name_age2.__name__} : {dog1_2.dog_name_age2()}")
# print(f"Output of {dog1_2.dog_name_age4.__name__} : {dog1_2.dog_name_age4()}")
# Below Method is Not recommended


class Dog2:
    """Dog2 class"""

    def dog_name_age(self, name, age):
        """Name of Age of the dog"""
        return f"Name of the dog is {name} and age is {age}"


dog2_1 = Dog2
dog2_2 = Dog2
print(dog2_1)
print(dog2_2)
print(dog2_1 == dog2_2)


# class Dog3:
#     """Dog3 class"""

#     @staticmethod
#     def dog_name_age(name, age):
#         """Name of Age of the dog"""
#         return f"Name of the dog is {name} and age is {age}"


# dog3 = Dog3
# print(dog3.dog_name_age("puppy", 3))
# print(Dog3.dog_name_age)
