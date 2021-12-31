from patterns.creational import abstract_factory, factory_method
from patterns.utils.menu import menu

patterns = {
    "abstract_factory": abstract_factory,
    "factory_method": factory_method,
}


def main():
    menu(__name__, patterns)


if __name__ == "__main__":
    main()
