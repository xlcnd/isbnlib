# -*- coding: utf-8 -*-
"""Query providers for metadata."""

import logging

from ._core import EAN13
from ._exceptions import NotRecognizedServiceError, NotValidISBNError
from .dev import cache

LOGGER = logging.getLogger(__name__)


@cache
def query(isbn, service='default'):
    """Query services like Google Books (JSON API), ... for metadata."""
    # validate inputs
    ean = EAN13(isbn)
    if not ean:
        LOGGER.critical('%s is not a valid ISBN', isbn)
        raise NotValidISBNError(isbn)
    isbn = ean
    # only import when needed
    from .registry import services

    if service != 'default' and service not in services:  # pragma: no cover
        LOGGER.critical('%s is not a valid service', service)
        raise NotRecognizedServiceError(service)
    meta = services[service](isbn)
    return meta or {}
