# -*- coding: utf-8 -*-
"""Get the cover of the book."""

import logging

try:                     # pragma: no cover
    # PY3
    from urllib.error import HTTPError, URLError
    from urllib.request import Request, urlopen
except ImportError:      # pragma: no cover
    # PY2
    from urllib2 import Request, urlopen, HTTPError, URLError

from json import loads

from .dev._exceptions import ISBNLibHTTPError, ISBNLibURLError
from .dev.webservice import query


COVERZOOM = 2
NOIMGSIZE = (15666, 16641, 2690)
UA = "isbnlib (gzip)"

LOGGER = logging.getLogger(__name__)


def bookid(isbn):
    """Return the Google's id associated with each ISBN."""
    from .registry import metadata_cache  # <-- dynamic
    # check the cache fist
    cache = metadata_cache
    if cache is not None:        # pragma: no cover
        key = 'gid' + isbn
        try:                     # pragma: no cover
            if cache[key]:
                return cache[key]
            else:
                raise  # <-- IMPORTANT: usually the caches don't return error!
        except:                  # pragma: no cover
            pass
    url = "https://www.googleapis.com/books/v1/volumes?q="\
          "isbn+{isbn}&fields=items/id&maxResults=1".format(isbn=isbn)
    content = query(url, user_agent=UA)
    try:
        content = loads(content)
        gid = content['items'][0]['id']
        if gid and cache is not None:
            cache[key] = gid
        return gid
    except:                      # pragma: no cover
        return


def _download(url, tofile=None):
    """Download image."""
    headers = {'User-Agent': UA, 'Pragma': 'no-cache'}
    request = Request(url, headers=headers)
    try:
        response = urlopen(request)
        LOGGER.debug('Request headers:\n%s', request.header_items())
    except HTTPError as e:  # pragma: no cover
        LOGGER.critical('ISBNLibHTTPError for %s with code %s [%s]',
                        url, e.code, e.msg)
        if e.code == 403:
            # Google uses this code when the image is not
            # available for any size (should use 404),
            # but also when you are blacklisted by the service
            LOGGER.debug('Cover not available or you are making many requests')
            return True     # <-- no more attempts to download
        if e.code in (401, 429):
            raise ISBNLibHTTPError('%s Are you are making many requests?'
                                   % e.code)
        if e.code in (502, 504):
            raise ISBNLibHTTPError('%s Service temporarily unavailable!'
                                   % e.code)
        raise ISBNLibHTTPError('(%s) %s' % (e.code, e.msg))
    except URLError as e:   # pragma: no cover
        LOGGER.critical('ISBNLibURLError for %s with reason %s',
                        url, e.reason)
        raise ISBNLibURLError(e.reason)
    content = response.read()
    noimageavailable = len(content) in NOIMGSIZE
    if noimageavailable:    # pragma: no cover
        return False
    if tofile:
        try:                # pragma: no cover
            # PY2
            content_type = response.info().getheader('Content-Type')
        except:             # pragma: no cover
            # PY3
            content_type = response.getheader('Content-Type')
        _, ext = content_type.split('/')
        tofile = tofile.split('.')[0] + '.' + ext.split('-')[-1]
        with open(tofile, 'wb') as f:
            f.write(content)
    else:                   # pragma: no cover
        print(content)
    return tofile


def _google_cover(gid, isbn, zoom=COVERZOOM, mode='prt'):
    """Download the cover from Google."""
    tpl = "http://books.google.com/books/content?id={gid}&printsec=frontcover"\
          "&img=1&zoom={zoom}&edge=curl&source=gbs_api"
    url = tpl.format(gid=gid, zoom=zoom)
    if mode == 'url':              # pragma: no cover
        return (url, None)
    coverfile = _download(url, tofile=isbn)
    while not coverfile:           # pragma: no cover
        # try a smaller resolution
        zoom -= 1
        if zoom > 0:
            url = tpl.format(gid=gid, zoom=zoom)
        else:
            return (None, None)
        coverfile = _download(url, tofile=isbn)
    return (url, coverfile) if coverfile and coverfile is not True\
        else (url, None)


def cover(isbn, size=COVERZOOM, mode='prt'):
    """Main entry point for cover."""
    gid = bookid(isbn)
    return _google_cover(gid, isbn, zoom=size, mode=mode) if gid\
        else (None, None)
