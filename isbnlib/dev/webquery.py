# -*- coding: utf-8 -*-
"""Base class to query a webservice and parse the result to py objects."""

import logging
import json
from . import webservice
from ._exceptions import DataNotFoundAtServiceError, ServiceIsDownError

UA = 'isbnlib (gzip)'
OUT_OF_SERVICE = 'Temporarily out of service'
BOOK_NOT_FOUND = 'No results match your search'
LOGGER = logging.getLogger(__name__)


class WEBQuery(object):

    """Base class to query a webservice and parse the result to py objects."""

    def __init__(self, service_url, ua=UA):
        """Initialize & call webservice."""
        self.url = service_url
        self.data = webservice.query(service_url, ua)

    def check_data(self, data_checker=None):  # pragma: no cover
        """Check the data & handle errors."""
        if data_checker:
            return data_checker(self.data)
        if self.data == '{}':
            LOGGER.warning('DataNotFoundAtServiceError for %s', self.url)
            raise DataNotFoundAtServiceError(self.url)
        if BOOK_NOT_FOUND in self.data:
            LOGGER.warning('DataNotFoundAtServiceError for %s', self.url)
            raise DataNotFoundAtServiceError(self.url)
        if OUT_OF_SERVICE in self.data:
            LOGGER.critical('ServiceIsDownError for %s', self.url)
            raise ServiceIsDownError(self.url)
        return True

    def parse_data(self, parser=json.loads):
        """Parse the data (default JSON -> PY)."""
        if parser is None:  # pragma: no cover
            return self.data
        return parser(self.data)   # <-- data is now unicode


def query(url, user_agent=UA, data_checker=None, parser=json.loads):
    """Put call and return the data from the web service."""
    wq = WEBQuery(url, user_agent)
    return wq.parse_data(parser) \
        if wq.check_data(data_checker) else None
