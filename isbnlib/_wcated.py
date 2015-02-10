# -*- coding: utf-8 -*-
"""Query the worldcat.org xID service for related ISBNs."""

import logging
from ast import literal_eval

from .dev._exceptions import DataWrongShapeError, NoDataForSelectorError
from .dev.webquery import query as wquery


LOGGER = logging.getLogger(__name__)
UA = 'isbnlib (gzip)'
SERVICE_URL = 'http://xisbn.worldcat.org/webservices/xid/isbn/{isbn}?'\
              'method=getEditions&format=python'


def _editions(isbn, data):
    """Return the records from the parsed response."""
    try:
        # put the selected data in records
        records = [ib['isbn'][0] for ib in data['list']]
    except:    # pragma: no cover
        try:
            extra = data['stat']
            LOGGER.debug('DataWrongShapeError for %s with data %s',
                         isbn, extra)
        except:
            raise DataWrongShapeError(isbn)
        raise NoDataForSelectorError(isbn)
    return records


def query(isbn):
    """Query the worldcat.org service for related ISBNs."""
    data = wquery(SERVICE_URL.format(isbn=isbn), UA, parser=literal_eval)
    return _editions(isbn, data)
