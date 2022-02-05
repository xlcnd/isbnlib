# -*- coding: utf-8 -*-
"""Query the Open Library for related ISBNs."""

import logging

from . import to_isbn13
from .dev._bouth23 import u
from .dev.webquery import query as wquery

LOGGER = logging.getLogger(__name__)
UA = 'isbnlib (gzip)'
SERVICE_URL = 'https://openlibrary.org/search.json?q={isbn}&fields=isbn'


# pylint: disable=broad-except
def query(isbn):
    """Query the Open Library for related ISBNs."""
    try:
        data = wquery(
            SERVICE_URL.format(isbn=isbn),
            user_agent=UA,
        )
        isbns = {u(to_isbn13(isbn)) for isbn in data['docs'][0]['isbn']}
    except Exception as ex:  # pragma: no cover
        LOGGER.debug(
            'No data from Open Library for isbn %s -- %s',
            isbn,
            str(ex),
        )
        return {to_isbn13(isbn)}
    return isbns
