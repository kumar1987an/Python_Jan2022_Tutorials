# dataclasses Module

from collections import namedtuple
from dataclasses import dataclass


@dataclass
class DataClassCard:
    """DataClassCard"""

    rank: str
    suit: str


queen_of_hearts = DataClassCard("Q", "Hearts")
print(queen_of_hearts)
print(queen_of_hearts.rank)
print(queen_of_hearts.suit)
print(queen_of_hearts == DataClassCard("Q", "Hearts"))


class NormalDataClassCard:
    """NormalDataClassCard"""

    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit


normal_queen_of_hearts = NormalDataClassCard("Q", "Hearts")
print(normal_queen_of_hearts)
print(normal_queen_of_hearts == NormalDataClassCard("Q", "Hearts"))


# Collections Module

Person = namedtuple("Person", ["age", "heigt", "name"])
dave = Person(20, 178, "Dave")
print(dave)
jack = Person(age=30, heigt=170, name="Jack S")
print(jack)
print(jack.name)
print(jack.heigt)
print(jack.age)
