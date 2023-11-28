from copy import deepcopy as _dc
from typing import TypeAliasType, TypeVar
from fishhook import hook

type Ref[T] = T
type Mut[Ref] = Ref[T]

class Trait[T]: ...

@hook(TypeAliasType | TypeVar)
def __invert__[T](self: T) -> Ref[T]:
    return Ref[self]

class Clone[T](Trait):
    def clone(self: Mut[T]) -> Mut[T]:
        return _dc(self)

class Example(Clone[int]): ...

x = Example()

user_functions = []

for trait_class in Trait.__subclasses__():
    for func in dir(trait_class):
        if callable(getattr(trait_class, func)) and not func.startswith("__"):
            user_functions.append(func)

def create_a_function(*args, **kwargs):

    def function_template(self, *args):
        raise NotImplementedError(f"{self.__class__.__name__} does not have this trait enabled.")

    return function_template

for i in user_functions:
    if_ = create_a_function()
    hook(object, func=if_, name=i)
