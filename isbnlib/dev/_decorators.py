# -*- coding: utf-8 -*-
"""Decorator for isbnlib."""
from functools import wraps


def cache(func):
    """Cache decorator."""
    # noqa
    @wraps(func)
    def memoized_func(*args, **kwargs):
        from ..registry import metadata_cache  # <-- dynamic and lazy

        cch = metadata_cache
        if cch is None:  # pragma: no cover
            return func(*args, **kwargs)

        # Persistent caches will NOT work IF
        # 'func' has callables in the arguments
        key = str(func.__name__) + str(args) + str(kwargs)

        if key in cch:
            return cch[key]
        else:
            value = func(*args, **kwargs)
            if value:
                cch[key] = value
            return value

    return memoized_func
