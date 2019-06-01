# -*- coding: utf-8 -*-
"""Query providers for metadata."""

from ._core import EAN13
from ._exceptions import NotRecognizedServiceError, NotValidISBNError

# TODO(v3.10) use @cache and delete parameter cache= on query


def query(isbn, service='default', cache='default'):
    """Query services like Google Books (JSON API), ... for metadata."""
    # validate inputs
    ean = EAN13(isbn)
    if not ean:
        raise NotValidISBNError(isbn)
    isbn = ean
    # only import when needed
    from .registry import services
    if service != 'default' and service not in services:  # pragma: no cover
        raise NotRecognizedServiceError(service)
    # set cache and get metadata
    if cache is None:  # pragma: no cover
        return services[service](isbn)
    if cache == 'default':  # pragma: no cover
        from .registry import metadata_cache
        cache = metadata_cache
    if cache is not None:
        key = isbn + service
        if key in cache:
            return cache[key]
    meta = services[service](isbn)
    if meta and cache is not None:  # pragma: no cover
        cache[key] = meta
    return meta if meta else {}
