from .types import Ref, Mut
from .traits import Trait, Clone
from .hooks import collect_user_functions, create_a_function, __invert__
from .examples import Example

# Apply hooks dynamically to classes after creation
for i in collect_user_functions():
    if_ = create_a_function()
    hook(object, func=if_, name=i)