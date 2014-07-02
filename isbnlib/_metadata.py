# -*- coding: utf-8 -*-
"""Query providers for metadata."""

from .registry import services
from ._exceptions import NotRecognizedServiceError


def query(isbn, service='default', cache=None):
    """Query worldcat.org, Google Books (JSON API), ... for metadata."""
    from .registry import metadata_cache
    if cache is None:
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
