"""
Abstract Factory lets you produce families of related
objects without specifying their concrete classes.

link: https://refactoring.guru/design-patterns/abstract-factory
"""
from abc import ABC, abstractmethod
from typing import Callable, Mapping

from patterns.application import Application


class Chair(ABC):
    """
    Chair is a product from the abstract factory.
    """

    @abstractmethod
    def has_legs(self) -> bool:
        ...

    def sit_on(self):
        print(f"Sitting on a {self.__class__.__name__}.")


class VictorianChair(Chair):
    def has_legs(self) -> bool:
        return True


class ModernChair(Chair):
    def has_legs(self) -> bool:
        return False

    def sit_on(self):
        super().sit_on()
        print("Wow! I am flywing!")


class Sofa(ABC):
    """
    Sofa is another product from the abstract factory.
    """

    @abstractmethod
    def lie_on(self):
        ...

    def sit_on(self):
        print(f"Sitting on a {self.__class__.__name__}.")


class VictorianSofa(Sofa):
    def lie_on(self):
        print("Lieing on a pretty sofa!")


class ModernSofa(Sofa):
    def lie_on(self):
        print("Lieing on a carpet!")

    def sit_on(self):
        super().sit_on()
        print("Wow! I am flywing!")


class FurnitureFactory(ABC):
    """
    The abstract factory declares creation types.
    """

    def __init__(self):
        self.__room = None

    @abstractmethod
    def create_chair(self) -> Chair:
        ...

    @abstractmethod
    def create_sofa(self) -> Sofa:
        ...

    def build(self):
        print(
            f"Building furnitures: "
            f"{self.create_chair().__class__.__name__} and "
            f"{self.create_sofa().__class__.__name__}"
        )


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> VictorianChair:
        return VictorianChair()

    def create_sofa(self) -> VictorianSofa:
        return VictorianSofa()


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> ModernChair:
        return ModernChair()

    def create_sofa(self) -> ModernSofa:
        return ModernSofa()


class AbstractFactoryApplication(Application):
    __factories: Mapping[str, Callable[[], FurnitureFactory]] = {
        "victorian": VictorianFurnitureFactory,
        "modern": ModernFurnitureFactory,
    }

    def main(self):
        """
        The client code chooses what factory it wants to instantiate, event not knowing
        the products types beforehand(the Sofa and Chair subclasses). The factory type is chosen
        usually at initialization stage.
        """
        while True:
            print()
            method: str = input(
                f"What category of furniture? (options are: {', '.join(self.__factories.keys())}): "
            )
            try:
                app = self.__factories[method]()
                app.build()
            except KeyError:
                print(f"Unnown delivery method: {method}")
                break


if __name__ == "__main__":
    AbstractFactoryApplication().main()
