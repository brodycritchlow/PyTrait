from .traits import Clone


class Example(Clone[int]):
    pass


x = Example()
