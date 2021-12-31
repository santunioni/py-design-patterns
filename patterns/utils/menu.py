from typing import Any, Mapping


def attempt_match(name: str, patterns: Mapping[str, Any]):
    module = patterns.get(name)
    if module is None:
        possible_keys = list(filter(lambda k: name in k, patterns.keys()))
        module = patterns[possible_keys.pop()]
    return module


def menu(patterns: Mapping[str, Any]):
    while True:
        pattern: str = input(f"What pattern? ({', '.join(patterns.keys())}): ")
        try:
            module = attempt_match(pattern, patterns)
            print("-" * 120)
            print(f"Initializing {module.__name__}.")
            print("-" * 120)
            module.main()
            print("-" * 120)
        except KeyError:
            print(f"Pattern {pattern} not found.")
            print()
            break
