# -*- coding: utf-8 -*-
"""Query providers for metadata."""

from .registry import services
from ._core import EAN13
from ._exceptions import NotRecognizedServiceError


def query(isbn, service='default', cache='UNDEFINED'):
    """Query worldcat.org, Google Books (JSON API), ... for metadata."""
    from .registry import metadata_cache           # <-- dinamic now!
    isbn = EAN13(isbn)
    if not isbn:
        return
    if cache == 'UNDEFINED':
        cache = metadata_cache
    if service != 'default' and service not in services:
        raise NotRecognizedServiceError(service)
    if cache is None:
        return services[service](isbn)
    key = isbn + service
    try:
        return cache[key]
    except:
        meta = services[service](isbn)
        if meta:
            cache[key] = meta
        return meta if meta else None
