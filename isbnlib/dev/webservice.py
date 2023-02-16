# -*- coding: utf-8 -*-
"""Query web services."""

import gzip
import logging
from io import BytesIO
from socket import timeout as sockettimeout

from ..config import options
from ._decorators import imcache
from ._exceptions import ISBNLibHTTPError, ISBNLibURLError, ServiceIsDownError

# pylint: disable=import-error
# pylint: disable=wrong-import-order
# pylint: disable=no-name-in-module
try:  # pragma: no cover
    from urllib.error import HTTPError, URLError
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen
except ImportError:  # pragma: no cover
    from urllib import urlencode

    from urllib2 import HTTPError, Request, URLError, urlopen

UA = 'isbnlib (gzip)'
LOGGER = logging.getLogger(__name__)


# pylint: disable=too-few-public-methods
# pylint: disable=useless-object-inheritance
class WEBService(object):
    """Class to query web services."""
    def __init__(self, url, user_agent=UA, values=None, appheaders=None):
        """Initialize main properties."""
        # TODO(use urllib.quote to the non-ascii part?)
        if not url.lower().startswith('http'):
            LOGGER.critical('Url (%s) not allowed!', url)
            raise ISBNLibURLError('Url (%s) not allowed!' % url)
        self._url = url
        # headers to accept gzipped content
        headers = {'Accept-Encoding': 'gzip', 'User-Agent': user_agent}
        # add more user provided headers
        if appheaders:  # pragma: no cover
            headers.update(appheaders)
        # if 'data' it does a POST request (data must be urlencoded)
        data = urlencode(values).encode('utf8') if values else None
        self._request = Request(url, data, headers=headers)

    def response(self):
        """Check errors on response."""
        # TODO(http 102)
        # How to handle "102 http's code"?
        # - urlopen doesn't catch a 102 code!
        #   https://docs.python.org/3/howto/urllib2.html#error-codes
        try:
            response = urlopen(
                self._request,
                timeout=options.get('URLOPEN_TIMEOUT'),
            )
            LOGGER.debug('Request headers:\n%s', self._request.header_items())
        except HTTPError as e:  # pragma: no cover
            LOGGER.critical(
                'ISBNLibHTTPError for %s with code %s [%s]',
                self._url,
                e.code,
                e.msg,
            )
            if e.code in (401, 403, 429):
                raise ISBNLibHTTPError('%s Are you making many requests?' %
                                       e.code)
            if e.code in (502, 504):
                raise ISBNLibHTTPError('%s Service temporarily unavailable!' %
                                       e.code)
            raise ISBNLibHTTPError('(%s) %s' % (e.code, e.msg))
        except URLError as e:  # pragma: no cover
            LOGGER.critical(
                'ISBNLibURLError for %s with reason %s',
                self._url,
                e.reason,
            )
            raise ISBNLibURLError(e.reason)
        except sockettimeout:  # pragma: no cover
            LOGGER.critical(
                'ServiceIsDownError for %s with reason %s',
                self._url,
                'timeout',
            )
            raise ServiceIsDownError('service timeout')
        return response if response else None

    def data(self):
        """Return the uncompressed data."""
        res = self.response()
        LOGGER.debug('Response headers:\n%s', res.info())
        if res.info().get('Content-Encoding') == 'gzip':
            buf = BytesIO(res.read())
            f = gzip.GzipFile(fileobj=buf)
            data = f.read()
        else:  # pragma: no cover
            data = res.read()
        return data.decode('utf-8', 'ignore')


@imcache
def query(url, user_agent=UA, values=None, appheaders=None):
    """Query to a web service."""
    service = WEBService(
        url,
        user_agent=user_agent,
        values=values,
        appheaders=appheaders,
    )
    data = service.data()
    LOGGER.debug('Raw data from service:\n%s', data)
    return data
