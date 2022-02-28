class BaseModel:

    """Repesent base model of the car"""

    rim = "normal"  # Class Attribute
    engine_liters = 1.5  # Class Attribute

    def engine_sound(self) -> str:  # instance method
        return "putt putt"

    def horn_sound(self) -> str:  # instance method
        return "beep, beep"

    def __repr__(self) -> str:  # instance method
        return f"This is a {__class__.__name__} class"


coop = BaseModel()
print(coop)
print(coop.rim)
print(coop.engine_liters)
print(coop.engine_sound())
print(coop.horn_sound())

print()


class Sport_Model(BaseModel):  # Class Inheritance
    engine_liters = 2.0
    rim = "Sport"

    def engine_sound(self) -> str:  # instance method
        return "VROOM VROOM"

    def horn_sound(self) -> str:  # instance method
        return "beep, beep".upper()

    def __repr__(self) -> str:  # instance method
        return f"{__class__.__name__}"


coop_sport = Sport_Model()
print(coop_sport)
print(coop_sport.rim)
print(coop_sport.engine_liters)
print(coop_sport.engine_sound())
print(coop_sport.horn_sound())

print()


class Luxury_Model(BaseModel):  # Inheritance
    rim = "Luxury"

    def engine_sound(self) -> str:  # instance method
        return "vroom vroom"

    def horn_sound(self) -> str:  # instance method
        return "honk, honk".upper()

    def __repr__(self) -> str:  # instance method
        return f"{__class__.__name__}"


print()

coop_luxury = Luxury_Model()
print(coop_luxury)
print(coop_luxury.rim)
print(coop_luxury.engine_liters)
print(coop_luxury.engine_sound())
print(coop_luxury.horn_sound())


class Luxury_Sport_Model(Luxury_Model, Sport_Model):
    def __repr__(self) -> str:  # instance method
        return f"{__class__.__name__}"


print()
coop_luxury_sport = Luxury_Sport_Model()
print(coop_luxury_sport)
print(coop_luxury_sport.rim)
print(coop_luxury_sport.engine_liters)
print(coop_luxury_sport.engine_sound())
print(coop_luxury_sport.horn_sound())


class Sport_Luxury_Model(Sport_Model, Luxury_Model):
    def __repr__(self) -> str:  # instance method
        return f"{__class__.__name__}"


print()
coop_sport_luxury = Sport_Luxury_Model()
print(coop_sport_luxury)
print(coop_sport_luxury.rim)
print(coop_sport_luxury.engine_liters)
print(coop_sport_luxury.engine_sound())
print(coop_sport_luxury.horn_sound())

print()
print(Sport_Luxury_Model.__mro__)


coop_custom = Sport_Luxury_Model()
coop_custom.rim = "custom"
print(coop_custom.rim)

coop_custom.brakes = "racing"

print(coop_custom.brakes)
BaseModel.brakes = "standard"
print(BaseModel.brakes)
