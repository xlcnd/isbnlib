# -*- coding: utf-8 -*-
"""Use Google to get an ISBN from words from title and author's name."""


import logging
from ._core import get_isbnlike, get_canonical_isbn
from .dev import webservice

LOGGER = logging.getLogger(__name__)


def goos(words):
    """Use Google to get an ISBN from words from title and author's name."""
    search_url = "http://www.google.com/search?q=%s+ISBN" % \
                 words.replace(' ', '+')
    user_agent = 'w3m/0.5.2'

    content = webservice.query(search_url, user_agent)
    isbns = get_isbnlike(content)

    for item in isbns:
        isbn = get_canonical_isbn(item, output='isbn13')
        if isbn:
            break
    if not isbn:    # pragma: no cover
        LOGGER.debug('No ISBN found for %s', words)
    return isbn if isbn else None
