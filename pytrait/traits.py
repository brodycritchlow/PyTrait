# pytrait/traits.py
from copy import deepcopy as _dc


class Trait[T]:
    ...

class Clone[T](Trait[T]):
    def clone(self: Mut[T]) -> Mut[T]:
        return _dc(self)
