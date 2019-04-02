from dataclasses import dataclass


def convert_years(orbital_period: float) -> float:
    def inner(self) -> float:
        return round(self.earth_years() / orbital_period, 2)
    return inner


@dataclass
class SpaceAge:
    seconds: int
    on_earth = convert_years(1)
    on_mercury = convert_years(0.2408467)
    on_venus = convert_years(0.61519726)
    on_mars = convert_years(1.8808158)
    on_jupiter = convert_years(11.862615)
    on_saturn = convert_years(29.447498)
    on_uranus = convert_years(84.016846)
    on_neptune = convert_years(164.79132)

    def earth_years(self) -> float:
        return self.seconds / 31557600
