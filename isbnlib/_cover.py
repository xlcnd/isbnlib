# -*- coding: utf-8 -*-
"""Get image links of the book's cover."""

import logging

from .dev._exceptions import NoDataForSelectorError
from .dev.webquery import query as wquery

LOGGER = logging.getLogger(__name__)

UA = "isbnlib (gzip)"
SERVICE_URL = 'https://www.googleapis.com/books/v1/volumes?q=isbn+{isbn}'\
              '&fields=items/volumeInfo(imageLinks)&maxResults=1'


def _get_img_lnks(isbn, data):
    """Get the image links."""
    try:
        select = data['items'][0]['volumeInfo']
    except:  # pragma: no cover
        LOGGER.debug('NoDataForSelectorError for %s', isbn)
        raise NoDataForSelectorError(isbn)
    return select.get('imageLinks', {}) if select else {}


def cover(isbn):
    """Main entry point for cover."""
    from .registry import metadata_cache  # <-- dynamic
    # check the cache first
    cache = metadata_cache
    if cache:  # pragma: no cover
        key = 'img-urls-' + isbn
        try:  # pragma: no cover
            if cache[key]:
                return cache[key]
            else:
                raise  # <-- IMPORTANT: usually the caches don't return error!
        except:  # pragma: no cover
            pass
    # request to the web service
    data = wquery(SERVICE_URL.format(isbn=isbn), user_agent=UA)
    lnks = _get_img_lnks(isbn, data) if data else {}
    if cache and lnks:  # pragma: no cover
        cache[key] = lnks
    return lnks
