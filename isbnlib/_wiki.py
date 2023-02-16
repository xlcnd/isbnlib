# -*- coding: utf-8 -*-
"""Query the wikipedia.org service for metadata."""

import logging
import re

from .dev import stdmeta
from .dev._exceptions import RecordMappingError
from .dev.webquery import query as wquery

UA = 'isbnlib (gzip)'
SERVICE_URL = 'https://en.wikipedia.org/api/rest_v1/data/citation/mediawiki/{isbn}'
LOGGER = logging.getLogger(__name__)


# pylint: disable=broad-except
def _mapper(isbn, records):
    """Map canonical <- records."""
    # canonical:
    # -> ISBN-13, Title, Authors, Publisher, Year, Language
    try:
        # mapping: canonical <- records
        canonical = {}
        canonical['ISBN-13'] = isbn
        canonical['Title'] = records.get('title', '').replace(' :', ':')
        # try to handle the inconsistent use of fields by Wikipedia (issue #65)!
        try:
            authors = [
                ' '.join(sublist)
                for sublist in records.get('author', [''])
            ]
            canonical['Authors'] = [
                author.replace('.', '') for author in authors
            ]
            buf = canonical.get('Authors', [])
            if not buf or len(buf[0]) == 0:
                raise IndexError
        except IndexError:
            try:
                authors = [
                    ' '.join(sublist)
                    for sublist in records.get('contributor', [''])
                ]
                canonical['Authors'] = [
                    author.replace('.', '') for author in authors
                ]
            except IndexError:
                pass
        canonical['Publisher'] = records.get('publisher', '') or ' '.join(
            [pub for pub in records.get('contributor', [''])[0] if pub])
        canonical['Year'] = ''
        strdate = records.get('date', '')
        if strdate:  # pragma: no cover
            match = re.search(r'\d{4}', strdate)
            if match:
                canonical['Year'] = match.group(0)
    except Exception:  # pragma: no cover
        LOGGER.debug('RecordMappingError for %s with data %s', isbn, records)
        raise RecordMappingError(isbn)
    # call stdmeta for extra cleaning and validation
    return stdmeta(canonical)


# pylint: disable=broad-except
def _records(isbn, data):
    """Classify (canonically) the parsed data."""
    try:
        # put the selected data in records
        records = data[0]
    except Exception:  # pragma: no cover
        # don't raise exception!
        LOGGER.debug('No data from "wikipedia" for isbn %s', isbn)
        return {}

    # map canonical <- records
    return _mapper(isbn, records)


def query(isbn):
    """Query the wikipedia.org service for metadata."""
    data = wquery(SERVICE_URL.format(isbn=isbn), user_agent=UA, throttling=0)
    return _records(isbn, data)
