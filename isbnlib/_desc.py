# -*- coding: utf-8 -*-
"""Return a small description of the book."""

from json import loads
from textwrap import fill

from .dev.webservice import query as wsquery


UA = "isbnlib (gzip)"


def goo_desc(isbn):
    """Get description from Google Books api."""
    from .registry import metadata_cache  # <-- dynamic
    cache = metadata_cache
    if cache is not None:                     # pragma: no cover
        key = 'gdesc' + isbn
        try:
            if cache[key]:
                return cache[key]
            else:
                raise  # <-- IMPORTANT: usually the caches don't return error!
        except:
            pass
    url = "https://www.googleapis.com/books/v1/volumes?q=isbn+{isbn}"\
          "&fields=items/volumeInfo(description)"\
          "&maxResults=1".format(isbn=isbn)
    content = wsquery(url, user_agent=UA)
    try:
        content = loads(content)
        content = content['items'][0]['volumeInfo']['description']
        content = fill(content, width=75) if content else None
        if content and cache is not None:     # pragma: no cover
            cache[key] = content
        return content
    except KeyError:                          # pragma: no cover
        return
