# -*- coding: utf-8 -*-
"""Query providers for metadata."""

from .registry import services, metadata_cache
from ._exceptions import NotRecognizedServiceError

CACHE = metadata_cache


def query(isbn, service='default', cache=CACHE):
    """Query worldcat.org, Google Books (JSON API), ... for metadata."""
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
