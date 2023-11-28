from typing import TypeVar, Generic

T = TypeVar('T')

Ref = Generic[T]
Mut = Ref[T]
# pytrait/traits.py
from copy import deepcopy as _dc

class Trait:
    ...

class Clone(Trait):
    def clone(self: 'Mut') -> 'Mut':
        return _dc(self)
from fishhook import hook

@hook(TypeVar)
def __invert__(self: T) -> 'Ref':
    return Ref[T]

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
from .traits import Clone

class Example(Clone):
    pass

x = Example()

# Apply hooks dynamically to classes after creation
for i in collect_user_functions():
    if_ = create_a_function()
    hook(object, func=if_, name=i)