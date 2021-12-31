"""
Factory Method provides an interface for creating objects in a superclass,
but allows subclasses to alter the type of objects that will be created.

link: https://refactoring.guru/design-patterns/factory-method
"""
from abc import ABC, abstractmethod
from typing import Callable, Mapping, MutableMapping


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


def main():
    """
    The client code chooses the delivery method, event not knowing
    the products types (the Transport subclasses).
    """
    factories: Mapping[str, Callable[[], Logistics]] = {
        "land": RoadLogistics,
        "sea": SeaLogistics,
    }
    apps: MutableMapping[str, Logistics] = {}
    while True:
        print()
        method: str = input(
            f"Deliever by? (options are: {', '.join(factories.keys())}): "
        )
        try:
            app = apps.get(method)
            if app is None:
                app = factories[method]()
                apps[method] = app
            app.plan_delivery()
        except KeyError:
            print(f"Unnown delivery method: {method}")
            break


if __name__ == "__main__":
    main()
