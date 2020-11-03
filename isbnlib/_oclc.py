# -*- coding: utf-8 -*-
"""Query the 'classify.oclc.org' service for classifiers."""

import logging
import re

from .dev import cache
from .dev._bouth23 import u
from .dev.webquery import query as wquery

UA = 'isbnlib (gzip)'
SERVICE_URL = 'http://classify.oclc.org/classify2/Classify?isbn={isbn}&maxRecs=1'
LOGGER = logging.getLogger(__name__)

RE_OWI = re.compile(r'owi="(.*?)"', re.I | re.M | re.S)
RE_OCLC = re.compile(r'oclc="(.*?)"', re.I | re.M | re.S)

RE_DDC = re.compile(r'<ddc>(.*?)</ddc>', re.I | re.M | re.S)
RE_LCC = re.compile(r'<lcc>(.*?)</lcc>', re.I | re.M | re.S)
RE_NSFA = re.compile(r'nsfa="(.*?)"', re.I | re.M | re.S)
RE_SFA = re.compile(r' sfa="(.*?)"', re.I | re.M | re.S)

RE_HEADINGS = re.compile(r'<headings>(.*?)</headings>', re.I | re.M | re.S)
RE_FLDS = re.compile(r' ident="(.*?)"', re.I | re.M | re.S)
RE_VALS = re.compile(r'fast">(.*?)</heading>', re.I | re.M | re.S)


def data_checker(xml):
    """Check the response from the service."""
    if not xml:
        LOGGER.debug("The service 'oclc' is temporarily down!")
        return False
    if 'response code="102"' in xml:
        LOGGER.debug("The service 'oclc' is temporarily very slow!")
        return False
    return True


def parser(xml):
    """Parse the response from the service."""
    if not xml:
        return {}  # pragma: no cover

    data = {}

    match = RE_OWI.search(u(xml))
    if match:
        data['owi'] = match.group(1)
    match = RE_OCLC.search(u(xml))
    if match:
        data['oclc'] = match.group(1)

    match = RE_LCC.search(u(xml))
    if match:
        buf = match.group()
        match = RE_SFA.search(buf)
        if match:
            data['lcc'] = match.group(1)

    match = RE_DDC.search(u(xml))
    if match:
        buf = match.group()
        match = RE_SFA.search(buf)
        if match:
            data['ddc'] = match.group(1)

    fast = parser_headings(xml)
    if fast:
        data['fast'] = fast

    return data


# pylint: disable=broad-except
def parser_headings(xmlthing):
    """RE parser for classify.oclc service (headings branch)."""
    match = RE_HEADINGS.search(u(xmlthing))
    if match:
        try:
            buf = match.group()
            flds = RE_FLDS.findall(buf)
            vals = RE_VALS.findall(buf)
            return dict(zip(flds, vals))
        except Exception:  # pragma: no cover
            LOGGER.debug("Bad parsing of 'headings' for 'oclc' service!")
    return {}  # pragma: no cover


@cache
def query_classify(isbn):
    """Query the classify.oclc service for classifiers."""
    return (wquery(
        SERVICE_URL.format(isbn=isbn),
        user_agent=UA,
        data_checker=data_checker,
        parser=parser,
    ) or {})
