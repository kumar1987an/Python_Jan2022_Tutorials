class BaseModel:

    """Repesent base model of the car"""

    trim = "normal"  # Class Attribute
    engine_liters = 1.5  # Class Attribute

    def engine_sound(self) -> str:  # instance method
        return "putt putt"

    def horn_sound(self) -> str:  # instance method
        return "beep, beep"

    def __repr__(self) -> str:  # instance method
        return f"{__class__.__name__}"


coupe = BaseModel()
print(coupe)
print(f"{coupe} has {coupe.trim} level")
print(f"{coupe} has a {coupe.engine_liters}L engine")
print(f"{coupe} engine sounds like {coupe.engine_sound()}")
print(f"{coupe} horn sounds like {coupe.horn_sound()}")


class Sport_Model(BaseModel):  # Inheritance
    engine_liters = 2.0
    trim = "Sport"

    def engine_sound(self) -> str:  # instance method
        return "VROOM VROOM"

    def horn_sound(self) -> str:  # instance method
        return "beep, beep".upper()

    def __repr__(self) -> str:  # instance method
        return f"{__class__.__name__}"


print()
coupe_sport = Sport_Model()
print(coupe_sport)
print(f"{coupe_sport} has {coupe_sport.trim} level")
print(f"{coupe_sport} has a {coupe_sport.engine_liters}L engine")
print(f"{coupe_sport} engine sounds like {coupe_sport.engine_sound()}")
print(f"{coupe_sport} horn sounds like {coupe_sport.horn_sound()}")


class Luxury_Model(BaseModel):  # Inheritance
    trim = "Luxury"

    def engine_sound(self) -> str:  # instance method
        return "vroom vroom"

    def horn_sound(self) -> str:  # instance method
        return "honk, honk".upper()

    def __repr__(self) -> str:  # instance method
        return f"{__class__.__name__}"


print()
coupe_luxury = Luxury_Model()
print(coupe_luxury)
print(f"{coupe_luxury} has {coupe_luxury.trim} level")
print(f"{coupe_luxury} has a {coupe_luxury.engine_liters}L engine")
print(f"{coupe_luxury} engine sounds like {coupe_luxury.engine_sound()}")
print(f"{coupe_luxury} horn sounds like {coupe_luxury.horn_sound()}")


class Luxury_Sport_Model(Luxury_Model, Sport_Model):
    def __repr__(self) -> str:  # instance method
        return f"{__class__.__name__}"


print()
coupe_luxury_sport = Luxury_Sport_Model()
print(coupe_luxury_sport)
print(f"{coupe_luxury_sport} has {coupe_luxury_sport.trim} level")
print(f"{coupe_luxury_sport} has a {coupe_luxury_sport.engine_liters}L engine")
print(f"{coupe_luxury_sport} engine sounds like {coupe_luxury_sport.engine_sound()}")
print(f"{coupe_luxury_sport} horn sounds like {coupe_luxury_sport.horn_sound()}")


class Sport_Luxury_Model(Sport_Model, Luxury_Model):
    def __repr__(self) -> str:  # instance method
        return f"{__class__.__name__}"


print()
coupe_sport_luxury = Sport_Luxury_Model()
print(coupe_sport_luxury)
print(f"{coupe_sport_luxury} has {coupe_sport_luxury.trim} level")
print(f"{coupe_sport_luxury} has a {coupe_sport_luxury.engine_liters}L engine")
print(f"{coupe_sport_luxury} engine sounds like {coupe_sport_luxury.engine_sound()}")
print(f"{coupe_sport_luxury} horn sounds like {coupe_sport_luxury.horn_sound()}")

print()
"""Custom Attributes"""
coupe_custom = Sport_Luxury_Model()
print(f"{coupe_custom} has {coupe_custom.trim} level")
coupe_custom.trim = "custom"
print(f"{coupe_custom} has {coupe_custom.trim} level")
print()
coupe_custom.brakes = "racing"
BaseModel.brakes = "standard"
print(f"{coupe_custom} has {coupe_custom.brakes} brakes")
print(f"{Sport_Luxury_Model.__name__} has {Sport_Luxury_Model.brakes} brakes")
