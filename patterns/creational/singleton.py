"""
Singleton lets you ensure that a class has only one instance,
while providing a lobal access point to this instance.

It is actually an antipattern, because singleton classes are hard to test.
However, there are variants in which client code can still create another object.

"We are all grown here"

link: https://refactoring.guru/design-patterns/singleton
"""


class SingletonMeta(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            instance = super().__call__(*args, **kwargs)
            cls.__instances[cls] = instance
        return cls.__instances[cls]


class Singleton(metaclass=SingletonMeta):
    """Classical approach: there is ALWAYS only one instance."""

    def __init__(self):
        self.a = "a"
        self.b = "b"


class DependencyManager:
    """
    Modern (not an antipattern) approach: you can create/use a global instance,
    but you can always instantiate new ones.

    This is a pythonic implementation of an object pool of size 1.

    The object pool itself should be a Singleton. We are using class
    attribute/method to mimic that.
    """

    __global_instance = None

    @classmethod
    def get_global_instance(cls) -> "DependencyManager":
        if cls.__global_instance is None:
            cls.__global_instance = DependencyManager()
        return cls.__global_instance


def singleton_assertions(singleton_factory):
    assert singleton_factory() is singleton_factory()
    s1, s2 = singleton_factory(), singleton_factory()
    assert s1 is s2
    s1.a = 1
    assert s2.a == 1
    assert singleton_factory().a == 1


def main():
    singleton_assertions(Singleton)
    singleton_assertions(DependencyManager.get_global_instance)


if __name__ == "__main__":
    main()
