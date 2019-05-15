# -*- coding: utf-8 -*-
"""Query providers for metadata."""

from ._core import EAN13
from ._exceptions import NotRecognizedServiceError, NotValidISBNError


def query(isbn, service='default', cache='default'):
    """Query services like Google Books (JSON API), ... for metadata."""
    # validate inputs
    ean = EAN13(isbn)
    if not ean:
        raise NotValidISBNError(isbn)
    isbn = ean
    # only import when needed (code splitting)
    from .registry import services
    if service != 'default' and service not in services:  # pragma: no cover
        raise NotRecognizedServiceError(service)
    # set cache and get metadata
    if cache is None:  # pragma: no cover
        return services[service](isbn)
    if cache == 'default':  # pragma: no cover
        from .registry import metadata_cache
        cache = metadata_cache
    key = isbn + service
    if key in cache:
        return cache[key]
    meta = services[service](isbn)
    if meta:  # pragma: no cover
        cache[key] = meta
    return meta if meta else {}
