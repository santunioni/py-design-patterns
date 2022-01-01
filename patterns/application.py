from __future__ import annotations

from abc import ABC
from typing import Callable, Mapping, TypeVar

Type = TypeVar("Type")


def attempt_match(name: str, patterns: Mapping[str, Type]) -> Type:
    module = patterns.get(name)
    if module is None:
        possible_keys = list(filter(lambda k: name in k, patterns.keys()))
        module = patterns[possible_keys.pop()]
    return module


def menu(patterns: Mapping[str, Callable[[], Application]]):
    while True:
        pattern: str = input(f"What pattern? ({', '.join(patterns.keys())}): ")
        try:
            application = attempt_match(pattern, patterns)()
            print("-" * 120)
            print(f"Initializing {application}.")
            print("-" * 120)
            application.main()
            print("-" * 120)
        except (KeyError, IndexError):
            print(f"Pattern {pattern} not found.")
            print()
            break


class Application(ABC):
    patterns: Mapping[str, Callable[[], Application]] = {}

    def main(self):
        menu(self.patterns)

    def __str__(self):
        return self.__class__.__name__

    def __del__(self):
        print(f"Exiting {self}")
