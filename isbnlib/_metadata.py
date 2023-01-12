# -*- coding: utf-8 -*-
"""Query providers for metadata."""

import logging
from importlib import import_module

from ._core import EAN13
from ._exceptions import NotRecognizedServiceError, NotValidISBNError
from .dev import cache

LOGGER = logging.getLogger(__name__)


def get_services():
    """Import 'services' only when needed."""
    reg = import_module('isbnlib.registry')
    return reg.services


@cache
def query(isbn, service='default'):
    """Query services like Google Books (JSON API), ... for metadata."""
    ean = EAN13(isbn)
    if not ean:
        LOGGER.critical('%s is not a valid ISBN', isbn)
        raise NotValidISBNError(isbn)
    isbn = ean
    services = get_services()
    if service not in services:  # pragma: no cover
        LOGGER.critical('%s is not a valid service', service)
        raise NotRecognizedServiceError(service)

    meta = services[service](isbn)
    return meta or {}
