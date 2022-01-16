# __iter__
# __next__

print(type(iter))
print(type(next))

print()


class IterationExample:
    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        y = self.x
        self.x += 1
        return y


classinstance = IterationExample()
element = iter(classinstance)

print(next(element))
print(next(element))
print(next(element))
print(next(element))
print(next(element))
print(next(element))
print(next(element))
print(next(element))
print(next(element))
print()

# for value in range(25):
#     print(next(element))


list1 = [
    0,
    5,
    10,
    15,
    20,
    100,
    10001,
    289834,
    753743,
    27777,
    163637384,
    746436,
    7,
    8,
    9,
    109,
]  # an iterable

element = iter(
    list1
)  # iter is a protocol or function which will instantiate the iteration

# print(next(element))
# print(next(element))
# print(next(element))
# print(element.__next__())
# print(element.__next__())

for x in element:
    print(x)

print()


class StopIterationclass:
    def __init__(self, max=0) -> None:
        self.max = max

    def __iter__(self):
        self.x = 1
        return self

    def __next__(self):
        if self.x <= self.max:
            val = 3 ** self.x
            self.x += 1
            return val
        else:
            raise StopIteration


y = StopIterationclass(3)
z = iter(y)
print(next(z))
print(next(z))
print(next(z))
print(next(z))
