# -*- coding: utf-8 -*-
# isort:skip_file
"""Decorator for isbnlib."""
from functools import wraps
from .._imcache import IMCache

im_cache = IMCache(maxlen=200)


def cache(func):
    """Cache decorator (cache)."""
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


def imcache(func):
    """Cache decorator (imcache)."""
    # noqa
    @wraps(func)
    def memoized_func(*args, **kwargs):
        cch = im_cache

        key = str(func.__name__) + str(args) + str(kwargs)

        if key in cch:
            return cch[key]
        else:
            value = func(*args, **kwargs)
            if value:
                cch[key] = value
            return value

    return memoized_func
