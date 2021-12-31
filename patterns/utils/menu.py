from typing import Any, Mapping


def menu(name: str, patterns: Mapping[str, Any]):
    while True:
        pattern: str = input(f"What pattern? ({', '.join(patterns.keys())}): ")
        try:
            print("-" * 120)
            print(f"Initializing {name}.{pattern}.")
            print("-" * 120)
            patterns[pattern].main()
            print("-" * 120)
        except KeyError:
            print(f"Pattern {pattern} not found. Finishing software.")
            break
