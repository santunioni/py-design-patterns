"""
Builder lets you construct complex objects step by step. The pattern allows you to produce
different types and representations of an object using the same construction code.

link: https://refactoring.guru/design-patterns/builder

The Builder pattern suggests that you extract the object con-
struction code out of its own class and move it to separate
objects called builders.

It requires at least the building steps of objects are related by a common interface (called Builder).

A builder can be implemented as singleton.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Mapping

from patterns.application import Application

PLACEHOLDER = object()


class Builder(ABC):
    @abstractmethod
    def reset(self):
        ...

    @abstractmethod
    def build_base(self):
        ...

    @abstractmethod
    def build_defenses(self):
        ...

    @abstractmethod
    def build_doors(self):
        ...

    @abstractmethod
    def build_top(self):
        ...

    @abstractmethod
    def build_extra(self):
        ...


@dataclass(slots=True)
class House:
    foundation: Any = None
    walls: Any = None
    doors: Any = None
    roof: Any = None
    windows: Any = None
    garage: Any = None
    swimming_pool: Any = None

    def __str__(self):
        return "FancyHouse" if self.garage and self.swimming_pool else "SimpleHouse"


class HouseBuilder(Builder):
    def __init__(self, **house_params):
        self.__house_params = house_params
        self._house = House()

    def reset(self):
        self._house = House()
        print(f"Start building a house. House params are: {self.__house_params}.")

    def build_base(self):
        """
        Implement some complex logic of building house foundation.
        """
        self._house.foundation = PLACEHOLDER
        print("Foundation was built.")

    def build_defenses(self):
        """
        Implement some complex logic of building house walls.
        """
        self._house.walls = PLACEHOLDER
        self._house.windows = PLACEHOLDER
        print("Walls and windows were built.")

    def build_doors(self):
        """
        Implement some complex logic of building house doors.
        """
        self._house.doors = PLACEHOLDER
        print("Doors were built.")

    def build_top(self):
        """
        Implement some complex logic of building house roofs.
        """
        self._house.roof = PLACEHOLDER
        print("Roof was built.")

    def build_extra(self):
        self._house.swimming_pool = PLACEHOLDER
        print("Swimming pool was built.")
        self._house.garage = PLACEHOLDER
        print("Garage pool was built.")

    def get_house(self) -> House:
        print(f"Delivering {self._house}.")
        return self._house


@dataclass(slots=True)
class Car:
    wheels: Any = None
    chassis: Any = None
    bodywork: Any = None
    doors: Any = None
    cover: Any = None
    air_conditioner: Any = None
    hidraulic: Any = None

    def __str__(self):
        return "FancyCar" if self.air_conditioner and self.hidraulic else "SimpleCar"


class CarBuilder(Builder):
    def __init__(self, **car_params):
        self.__car_params = car_params
        self._car: Car = Car()

    def reset(self):
        self._car = Car()
        print(f"Start building a car. Car params are: {self.__car_params}.")

    def build_base(self):
        """
        Implement some complex logic of building car foundation.
        """
        self._car.chassis = PLACEHOLDER
        print("Chassis built.")
        self._car.wheels = PLACEHOLDER
        print("Wheels placed.")

    def build_defenses(self):
        """
        Implement some complex logic of building car bodywork.
        """
        self._car.bodywork = PLACEHOLDER

    def build_doors(self):
        """
        Implement some complex logic of building car doors.
        """
        self._car.doors = PLACEHOLDER
        print("Doors built and placed.")

    def build_top(self):
        """
        Implement some complex logic of building car roofs.
        """
        self._car.cover = PLACEHOLDER
        print("Roof built and placed.")

    def build_extra(self):
        """
        Implement some complex logic of building car air conditioner and hidraulic.
        """
        self._car.air_conditioner = PLACEHOLDER
        print("Air coudntioner built and placed.")
        self._car.hidraulic = PLACEHOLDER
        print("Hidraulic built.")

    def get_car(self) -> Car:
        print(f"Delivering {self._car}.")
        return self._car


class ConstructionDirector:
    def __init__(self, builder: Builder):
        self.__builder = builder

    def change_builder(self, builder: Builder):
        self.__builder = builder

    def make(self, fancy: bool):
        self.__builder.reset()
        self.__builder.build_base()
        self.__builder.build_defenses()
        self.__builder.build_doors()
        self.__builder.build_top()
        if fancy:
            self.__builder.build_extra()


class BuilderApplication(Application):

    __fancy: Mapping[str, bool] = {
        "y": True,
        "n": False,
    }

    def __instruct(self, builder: Builder):
        director = ConstructionDirector(builder)
        fancy = self.__fancy[(input("Fancy? (y/N) ") or "n")[0].lower()]
        print()
        director.make(fancy)

    def main(self):
        while True:
            print()
            product: str = input("Want to build what? (options are: car, house): ")

            if product == "car":
                builder = CarBuilder(wheels=4)
                self.__instruct(builder)
                _ = builder.get_car()
                continue
            if product == "house":
                builder = HouseBuilder(color="yellow")
                self.__instruct(builder)
                _ = builder.get_house()
                continue

            print(f"Unknown product: {product}")
            break


if __name__ == "__main__":
    BuilderApplication().main()
