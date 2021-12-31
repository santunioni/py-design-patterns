from patterns.application import Application
from patterns.creational.abstract_factory import AbstractFactoryApplication
from patterns.creational.factory_method import FactoryMethodApplication


class CreationalPatterns(Application):

    patterns = {
        "abstract_factory": AbstractFactoryApplication,
        "factory_method": FactoryMethodApplication,
    }


if __name__ == "__main__":
    CreationalPatterns().main()
