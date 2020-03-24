# -*- coding: utf-8 -*-
"""Return a small description of the book."""

import logging
from json import loads
from textwrap import fill

from .dev import cache
from .dev.webservice import query as wsquery

LOGGER = logging.getLogger(__name__)

UA = 'isbnlib (gzip)'
SERVICE_URL = ('https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}'
               '&fields=items/volumeInfo(description)'
               '&maxResults=1')


# pylint: disable=broad-except
@cache
def goo_desc(isbn):
    """Get description from Google Books api."""
    url = SERVICE_URL.format(isbn=isbn)
    content = wsquery(url, user_agent=UA)
    try:
        content = loads(content)
        content = content['items'][0]['volumeInfo']['description']
        # TODO(MV) don't format content here!
        content = fill(content, width=75) if content else ''
        return content
    except Exception:  # pragma: no cover
        LOGGER.debug('No description for %s', isbn)
        return ''
