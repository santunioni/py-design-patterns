"""
Singleton lets you ensure that a class has only one instance,
while providing a lobal access point to this instance.

It is actually an antipattern, because singleton classes are hard to test.
However, there are variants in which client code can still create another object.

"We are all grown here"

link: https://refactoring.guru/design-patterns/singleton
"""
import logging

logger = logging.getLogger(__name__)


class SingletonMeta(type):
    """
    Using this class as metaclass is THE BEST approach for Singletons in python.
    """

    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            instance = super().__call__(*args, **kwargs)
            cls.__instances[cls] = instance
        return cls.__instances[cls]

    @classmethod
    def reset(mcs):
        mcs.__instances = {}


class Singleton(metaclass=SingletonMeta):
    """Classical approach: there is ALWAYS only one instance."""

    def __init__(self):
        self.a = "a"
        self.b = "b"


class SingletonParent:
    """
    Singleton implementations based on inheriting this class don't work well, because:

    If your class is initializing something, the interpreter will call the initializer (__init__) everytime you
    attempt to instantiate it, even if you are always returning the same instance. The `single_assertions` function
    tests this behavior and tells us this class fails.
        This can cause the following unwanted behavior in production:
            Resetting the instance to initial state if your class is multable whenever you attempt to instantiate it.
            (multable singletons is an antipattern)
        Exaust the resources your initializer requires (database connections, for example).
    """

    @classmethod
    def reset(cls):
        if hasattr(cls, "instance"):
            del cls.instance

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(SingletonParent, cls).__new__(cls, *args, **kwargs)
        return cls.instance


class FlawedSingleton1(SingletonParent):
    """
    This Singleton calls the initializer __init__ each time you attempt to instantiate it.
    Check this at the singleton_assertions function.
    """

    def __init__(self):
        self.a = "a"
        self.b = "b"


class FlawedSingleton2(SingletonParent):
    """
    This Singleton only works well because it doesn't have an initializer.
    """


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

    @classmethod
    def reset(cls):
        cls.__global_instance = None


def reset_all_singletons():
    for cls in (SingletonMeta, SingletonParent, DependencyManager):
        cls.reset()


def singleton_assertions(singleton_factory):
    """
    Performs a couple of assertions in a singleton_factory
    to assure it creates good singletons.
    """
    reset_all_singletons()

    # Basic singleton functionality: you can´t instantiate new objects.
    assert singleton_factory() is singleton_factory()

    # Mutating s1 should also mutate s2 because they are the same object.
    s1, s2 = singleton_factory(), singleton_factory()
    s1.a = 1
    assert s2.a == 1

    # "Instantiating" the singleton class again shouldn´t reset the singleton object state.
    assert singleton_factory().a == 1


def test_good_singletons(good_singleton_factories):
    """
    Assures the all single factories tested here success at all the
    singleton assertions in the singleton_assertions function.
    """
    for singleton_factory in good_singleton_factories:
        singleton_assertions(singleton_factory)


def test_bad_singletons(bad_singleton_factories):
    """
    Assures the all single factories tested here fail at least one of the
    singleton assertions in the singleton_assertions function.
    """
    for singleton_factory in bad_singleton_factories:
        failed = False
        try:
            singleton_assertions(singleton_factory)
        except AssertionError as err:
            logger.exception(err)
            failed = True
        assert failed


def main():
    test_good_singletons(
        [
            Singleton,
            DependencyManager.get_global_instance,
            FlawedSingleton2,
        ]
    )
    test_bad_singletons([FlawedSingleton1])


if __name__ == "__main__":
    main()
