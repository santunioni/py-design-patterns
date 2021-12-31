"""
Factory Method provides an interface for creating objects in a superclass,
but allows subclasses to alter the type of objects that will be created.
"""
from abc import ABC, abstractmethod
from typing import Mapping, Type


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


class Application:

    apps: Mapping[str, Type[Logistics]] = {"land": RoadLogistics, "sea": SeaLogistics}

    @classmethod
    def main(cls):
        """
        The client code chooses the delivery method, event not knowing
        the products types (the Transport subclasses).
        """
        while True:
            method = input(
                f"\nDeliever by? (options are: {', '.join(cls.apps.keys())})\n"
            )
            try:
                app = cls.apps[method]()
                app.plan_delivery()
            except KeyError:
                print(f"Unnown delivery method: {method}")
                break


if __name__ == "__main__":
    Application.main()
