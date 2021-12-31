"""
Factory Method provides an interface for creating objects in a superclass,
but allows subclasses to alter the type of objects that will be created.

link: https://refactoring.guru/design-patterns/factory-method
"""
from abc import ABC, abstractmethod
from typing import Callable, Mapping

from patterns.application import Application


class Transport(ABC):
    """
    All products created by creator subclasses factory method
    should implement this interface.

    """

    @abstractmethod
    def deliver(self):
        ...


class Truck(Transport):
    def deliver(self):
        print("Delivering cargo by land ...")


class Ship(Transport):
    def deliver(self):
        print("Delivering cargo by sea ...")


class Logistics(ABC):
    """The creator class of the FactoryMethod pattern.
    Responsible for creating a generic object."""

    def __str__(self):
        return "Logistics app"

    def __del__(self):
        print(f"Exiting {self.__class__.__name__} app.")

    @abstractmethod
    def create_transport(self) -> Transport:
        """
        Method for creating transport (the product).
        May return some default type, otherwise should be an abstract method.
        """

    def plan_delivery(self):
        """
        Represents some business logic dependent on the factory method.
        """
        print(f"\n{self} is planing the delivery")
        transport = self.create_transport()
        transport.deliver()
        print("Cargo delivered.")


class RoadLogistics(Logistics):
    def create_transport(self) -> Truck:
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self) -> Ship:
        return Ship()


class FactoryMethodApplication(Application):

    __factories: Mapping[str, Callable[[], Logistics]] = {
        "land": RoadLogistics,
        "sea": SeaLogistics,
    }

    def main(self):
        """
        The client code chooses the delivery method, but is not required to depend on concrete
        classes of the product types (the Transport subclasses).
        """
        while True:
            print()
            method: str = input(
                f"Deliever by? (options are: {', '.join(self.__factories.keys())}): "
            )
            try:
                app = self.__factories[method]()
                app.plan_delivery()
            except KeyError:
                print(f"Unnown delivery method: {method}")
                break


if __name__ == "__main__":
    FactoryMethodApplication().main()
