from typing import TypeAliasType, TypeVar

from fishhook import hook

from .traits import Trait


@hook(TypeAliasType | TypeVar)
def __invert__[T](self: T) -> Ref[T]:
    return Ref[self]

def collect_user_functions():
    user_functions = []
    for trait_class in Trait.__subclasses__():
        for func in dir(trait_class):
            if callable(getattr(trait_class, func)) and not func.startswith("__"):
                user_functions.append(func)
    return user_functions

def create_a_function(*args, **kwargs):
    def function_template(self, *args):
        raise NotImplementedError(f"{self.__class__.__name__} does not have this trait enabled.")
    return function_template
