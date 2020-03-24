# -*- coding: utf-8 -*-
"""Get image links of the book's cover."""

import logging

from .dev import cache
from .dev.webquery import query as wquery

LOGGER = logging.getLogger(__name__)

UA = 'isbnlib (gzip)'
SERVICE_URL = ('https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}'
               '&fields=items/volumeInfo(imageLinks)&maxResults=1')


@cache
def cover(isbn):
    """Get the urls for covers from Google Books."""
    data = wquery(SERVICE_URL.format(isbn=isbn), user_agent=UA)
    urls = {}
    try:
        urls = data['items'][0]['volumeInfo']['imageLinks']
    except (KeyError, IndexError):  # pragma: no cover
        LOGGER.debug('No cover img data for %s', isbn)
    return urls
