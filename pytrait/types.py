from typing import Generic, TypeVar

T = TypeVar('T')

Ref = Generic[T]
Mut = Ref[T]
