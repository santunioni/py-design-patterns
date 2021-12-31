from typing import Callable, Mapping

from patterns.application import Application, attempt_match
from patterns.behavioral import BehavioralPatterns
from patterns.creational import CreationalPatterns
from patterns.structural import StructuralPatterns


class Main:

    __app_factories: Mapping[str, Callable[[], Application]] = {
        "creational": CreationalPatterns,
        "behavioral": BehavioralPatterns,
        "structural": StructuralPatterns,
    }

    def __new__(cls):
        print("Welcome to the design patterns CLI.")
        print()
        while True:
            pattern_type: str = input(
                f"Which type? ({', '.join(cls.__app_factories.keys())}): "
            )
            try:
                app = attempt_match(pattern_type, cls.__app_factories)()
                app.main()
            except (KeyError, IndexError):
                print(f"Type {pattern_type} not found. Finishing software.")
                break


main = Main
if __name__ == "__main__":
    main()
