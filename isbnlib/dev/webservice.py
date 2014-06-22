# -*- coding: utf-8 -*-
"""Query web services."""

import logging
import gzip
from .bouth23 import s, bstream
try:                     # pragma: no cover
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError, URLError
except ImportError:      # pragma: no cover
    from urllib import urlencode
    from urllib2 import Request, urlopen, HTTPError, URLError
from ._exceptions import ISBNToolsHTTPError, ISBNToolsURLError

UA = 'webservice (gzip)'
LOGGER = logging.getLogger(__name__)


class WEBService(object):

    """Class to query web services."""

    def __init__(self, url, user_agent=UA, values=None):
        """Initialize main properties."""
        self._url = url
        # headers to accept gzipped content
        headers = {'Accept-Encoding': 'gzip', 'User-Agent': user_agent}
        # if 'data' it does a PUT request (data must be urlencoded)
        data = urlencode(values) if values else None
        self._request = Request(url, data, headers=headers)
        self.response = None

    def _response(self):
        try:
            self.response = urlopen(self._request)
        except HTTPError as e:  # pragma: no cover
            LOGGER.critical('ISBNToolsHTTPError for %s with code %s',
                            self._url, e.code)
            raise ISBNToolsHTTPError(e.code)
        except URLError as e:   # pragma: no cover
            LOGGER.critical('ISBNToolsURLError for %s with reason %s',
                            self._url, e.reason)
            raise ISBNToolsURLError(e.reason)

    def data(self):
        """Return the uncompressed data."""
        self._response()
        if self.response.info().get('Content-Encoding') == 'gzip':
            buf = bstream(self.response.read())
            f = gzip.GzipFile(fileobj=buf)
            data = f.read()
        else:                   # pragma: no cover
            data = self.response.read()
        return s(data)


def query(url, user_agent=UA, values=None):
    """Query to a web service."""
    service = WEBService(url, user_agent, values)
    return service.data()
