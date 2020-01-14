# -*- coding: utf-8 -*-
"""Query providers for metadata."""

from ._core import EAN13
from ._exceptions import NotRecognizedServiceError, NotValidISBNError
from .dev import cache


@cache
def _get_meta(provider, isbn):
    return provider(isbn)


def query(isbn, service='default'):
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
    provider = services[service]
    meta = _get_meta(provider, isbn)
    return meta if meta else {}
