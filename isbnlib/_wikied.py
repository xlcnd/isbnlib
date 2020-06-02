# -*- coding: utf-8 -*-
"""Query the wikipedia.org service for related ISBNs."""

import logging

from ._core import to_isbn13
from .dev.webquery import query as wquery

UA = 'isbnlib (gzip)'
SERVICE_URL = 'https://en.wikipedia.org/api/rest_v1/data/citation/mediawiki/{isbn}'
LOGGER = logging.getLogger(__name__)


# pylint: disable=broad-except
def _parser(isbn, data):
    """Parse the response from the Wikipedia service."""
    editions = [to_isbn13(isbn)]
    try:
        records = data[0].get('ISBN', [])
        eds = {to_isbn13(isbn) for isbn in records}
        editions.extend(eds)
    except Exception:  # pragma: no cover
        LOGGER.debug('No data from "wikipedia" for isbn %s', isbn)
    return editions


def query(isbn):
    """Query the wikipedia.org service for 'editions'."""
    data = wquery(SERVICE_URL.format(isbn=isbn), user_agent=UA, throttling=0)
    return set(_parser(isbn, data))
