# -*- coding: utf-8 -*-
"""Query the worldcat.org 'classify.oclc.org' service for metadata."""

import logging
import re

from .dev import stdmeta
from .dev._bouth23 import u
from .dev._exceptions import (NoDataForSelectorError, RecordMappingError)
from .dev.webquery import query as wquery

UA = 'isbnlib (gzip)'
SERVICE_URL = 'http://classify.oclc.org/classify2/Classify?isbn={isbn}'\
              '&maxRecs=1&summary=true'
LOGGER = logging.getLogger(__name__)

RE_FLDS = re.compile(r'\s([a-z]+)="', re.I | re.M | re.S)
RE_VALS = re.compile(r'="(.*?)"', re.I | re.M | re.S)
RE_WORK = re.compile(r'<work .*/>', re.I | re.M | re.S)


def _clean(txt):
    """Util function to clean Author strings."""
    # delete annotations
    txt = re.sub(r'\[.*\]', '', txt)
    txt = re.sub(r'\(.*\)', '', txt)
    txt = re.sub(r'[0-9]{4}\s*\-*[0-9]{0,4}', '', txt)
    # delete abbreviations
    txt.strip('. ')
    # std name
    txt.strip(', ')
    if ',' in txt:
        txt = ' '.join(x.strip() for x in txt.split(',')[::-1])
    return txt.strip()


def _mapper(isbn, records):
    """Mapp: canonical <- records."""
    # canonical: ISBN-13, Title, Authors, Publisher, Year, Language
    try:
        canonical = {}
        canonical['ISBN-13'] = u(isbn)
        canonical['Title'] = records.get('title', u('')).replace(' :', ':')
        buf = records.get('author', u(''))
        canonical['Authors'] = [_clean(x) for x in buf.split('|')]
        canonical['Publisher'] = records.get('publisher', u(''))
        canonical['Year'] = records.get('hyr', u('')) or records.get('lyr',
                                                                     u(''))
        canonical['Language'] = records.get('lang', u(''))
    except:  # pragma: no cover
        LOGGER.debug("RecordMappingError for %s with data %s", isbn, records)
        raise RecordMappingError(isbn)
    # call stdmeta for extra cleanning and validation
    return stdmeta(canonical)


def _records(isbn, data):
    """Classify (canonically) the parsed data."""
    # check data
    if not data:
        LOGGER.debug('NoDataForSelectorError for %s', isbn)
        raise NoDataForSelectorError(isbn)
    # map canonical <- records
    return _mapper(isbn, data)


def reparser(xmlthing):
    """RE parser for classify.oclc service."""
    match = RE_WORK.search(u(xmlthing))
    if match:
        try:
            buf = match.group()
            flds = RE_FLDS.findall(buf)
            vals = RE_VALS.findall(buf)
            return dict(zip(flds, vals))
        except:
            # FIXME
            pass
    return


def query(isbn):
    """Query the worldcat.org service for metadata."""
    data = wquery(
        SERVICE_URL.format(isbn=isbn),
        user_agent=UA,
        data_checker=None,
        parser=reparser)
    return _records(isbn, data)
