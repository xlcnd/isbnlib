# -*- coding: utf-8 -*-
"""Use Google to get an ISBN from words from title and author's name."""

import logging

from ._core import get_canonical_isbn, get_isbnlike
from .dev import cache, webservice

try:  # pragma: no cover
    from urllib.parse import quote
except ImportError:  # pragma: no cover
    from urllib import quote

LOGGER = logging.getLogger(__name__)


@cache
def goos(words):
    """Use Google to get an ISBN from words from title and author's name."""
    service_url = 'http://www.google.com/search?q=ISBN+'
    search_url = service_url + quote(words.replace(' ', '+'))

    user_agent = 'w3m/0.5.3'

    content = webservice.query(
        search_url,
        user_agent=user_agent,
        appheaders={
            'Content-Type': 'text/plain; charset="UTF-8"',
            'Content-Transfer-Encoding': 'Quoted-Printable',
        },
    )
    isbns = get_isbnlike(content)
    isbn = ''
    try:
        for item in isbns:
            isbn = get_canonical_isbn(item, output='isbn13')
            if isbn:  # pragma: no cover
                break
    except IndexError:  # pragma: no cover
        pass
    if not isbns or not isbn:  # pragma: no cover
        LOGGER.debug('No ISBN found for %s', words)
    return isbn
