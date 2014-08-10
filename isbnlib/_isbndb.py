# -*- coding: utf-8 -*-
"""Query the isbndb.org service for metadata."""

import logging
import re
from .dev.webquery import query as wquery
from .dev import stdmeta
from .dev.bouth23 import u
from .config import apikeys
from .dev._exceptions import (DataWrongShapeError,
                              NoDataForSelectorError,
                              RecordMappingError, NoAPIKeyError)


UA = 'isbnlib (gzip)'
SERVICE_URL = 'http://isbndb.com/api/v2/json/{apikey}/book/{isbn}'
PATT_YEAR = re.compile(r'\d{4}')
LOGGER = logging.getLogger(__name__)


def _mapper(isbn, records):
    """Map canonical <- records."""
    # canonical:
    # -> ISBN-13, Title, Authors, Publisher, Year, Language
    try:
        # mapping: canonical <- records
        canonical = {}
        canonical['ISBN-13'] = u(isbn)
        # assert isbn == records['isbn13'], "isbn was mungled!"
        canonical['Title'] = records.get('title', u(''))
        authors = [a['name'] for a in records['author_data']]
        canonical['Authors'] = authors
        canonical['Publisher'] = records.get('publisher_name', u(''))
        canonical['Year'] = u('')
        if 'edition_info' in records:
            match = re.search(PATT_YEAR, records['edition_info'])
            if match:
                canonical['Year'] = str(match.group(0))
        canonical['Language'] = records.get('language', u(''))
    except:
        raise RecordMappingError(isbn)
    # call stdmeta for extra cleanning and validation
    return stdmeta(canonical)


def _records(isbn, data):
    """Classify (canonically) the parsed data."""
    try:
        # put the selected data in records
        records = data['data'][0]
    except:
        try:
            extra = data['error']
            LOGGER.debug('DataWrongShapeError for %s with data %s',
                         isbn, extra)
        except:
            raise DataWrongShapeError(isbn)
        raise NoDataForSelectorError(isbn)

    # map canonical <- records
    return _mapper(isbn, records)


def query(isbn):
    """Query the isbndb.org service for metadata."""
    if not apikeys.get('isbndb'):
        raise NoAPIKeyError
    data = wquery(SERVICE_URL.format(apikey=apikeys['isbndb'], isbn=isbn), UA)
    return _records(isbn, data)
