# -*- coding: utf-8 -*-
"""Query providers for metadata."""

from ._core import EAN13
from ._exceptions import NotRecognizedServiceError, NotValidISBNError
from .registry import services


def query(isbn, service='default', cache='default'):
    """Query worldcat.org, Google Books (JSON API), ... for metadata."""
    from .registry import metadata_cache  # <-- dinamic now!
    ean = EAN13(isbn)  # <-- XXX maybe this is too strict?
    if not ean:
        raise NotValidISBNError(isbn)
    isbn = ean
    if service != 'default' and service not in services:  # pragma: no cover
        raise NotRecognizedServiceError(service)
    if cache is None:  # pragma: no cover
        return services[service](isbn)
    if cache == 'default':
        cache = metadata_cache
    key = isbn + service
    try:
        if cache[key]:
            return cache[key]
        else:  # pragma: no cover
            raise  # <-- IMPORTANT: usually the caches don't return error!
    except:
        meta = services[service](isbn)
        if meta:
            cache[key] = meta
        return meta if meta else None
