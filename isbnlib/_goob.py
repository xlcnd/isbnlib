# -*- coding: utf-8 -*-
"""Query the Google Books (JSON API v1) service for metadata."""

import logging
from .dev.webquery import query as wquery
from .dev import stdmeta
from .dev.bouth23 import u
from .dev._exceptions import (DataWrongShapeError,
                              NoDataForSelectorError,
                              RecordMappingError)

UA = 'isbnlib (gzip)'
SERVICE_URL = 'https://www.googleapis.com/books/v1/volumes?q=isbn+{isbn}'\
    '&fields=items/volumeInfo(title,authors,publisher,publishedDate,language)'\
    '&maxResults=1'
LOGGER = logging.getLogger(__name__)


def _mapper(isbn, records):
    """Mapp: canonical <- records."""
    # canonical: ISBN-13, Title, Authors, Publisher, Year, Language
    try:
        canonical = {}
        canonical['ISBN-13'] = u(isbn)
        canonical['Title'] = records.get('title', u('')).replace(' :', ':')
        canonical['Authors'] = records.get('authors', [u('')])
        canonical['Publisher'] = records.get('publisher', u(''))
        if 'publishedDate' in records \
           and len(records['publishedDate']) >= 4:
            canonical['Year'] = records['publishedDate'][0:4]
        else:         # pragma: no cover
            canonical['Year'] = u('')
        canonical['Language'] = records.get('language', u(''))
    except:           # pragma: no cover
        raise RecordMappingError(isbn)
    # call stdmeta for extra cleanning and validation
    return stdmeta(canonical)


def _records(isbn, data):
    """Classify (canonically) the parsed data."""
    try:
        # put the selected data in records
        records = data['items'][0]['volumeInfo']
    except:           # pragma: no cover
        try:
            extra = data['stat']
            LOGGER.debug('DataWrongShapeError for %s with data %s',
                         isbn, extra)
        except:
            raise DataWrongShapeError(isbn)
        raise NoDataForSelectorError(isbn)

    # map canonical <- records
    return _mapper(isbn, records)


def query(isbn):
    """Query the Google Books (JSON API v1) service for metadata."""
    data = wquery(SERVICE_URL.format(isbn=isbn), UA)
    return _records(isbn, data)
