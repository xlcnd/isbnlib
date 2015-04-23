# -*- coding: utf-8 -*-
"""Return editions for a given ISBN."""

import logging

from ._core import EAN13
from ._exceptions import NotRecognizedServiceError, NotValidISBNError
from ._thinged import query as ted
from ._wcated import query as wed

PROVIDERS = ('any', 'merge', 'thingl', 'wcat')
TRUEPROVIDERS = ('wcat', 'thingl')  # <-- by priority
LOGGER = logging.getLogger(__name__)


def fake_provider_any(isbn):
    """Fake provider 'any' service."""
    providers = {'wcat': wed, 'thingl': ted}
    for provider in TRUEPROVIDERS:
        data = []
        try:
            data = providers[provider](isbn)
            if data:
                return data
            continue       # pragma: no cover
        except:            # pragma: no cover
            continue
    return data            # pragma: no cover


def fake_provider_merge(isbn):
    """Fake provider 'merge' service."""
    data = []
    try:                   # pragma: no cover
        wdata = wed(isbn)
        if wdata:
            tdata = ted(isbn)
            if tdata:
                data = list(set(wdata + tdata))
                return data
        raise
    except:                # pragma: no cover
        return data


def editions(isbn, service='wcat'):
    """Return the list of ISBNs of editions related with this ISBN."""
    isbn = EAN13(isbn)
    if not isbn:
        LOGGER.critical('%s is not a valid ISBN', isbn)
        raise NotValidISBNError(isbn)

    if service == 'any':
        return fake_provider_any(isbn)

    if service == 'merge':
        return fake_provider_merge(isbn)

    if service not in PROVIDERS:
        LOGGER.critical('%s is not a recognized editions provider', service)
        raise NotRecognizedServiceError(service)
    return wed(isbn) if service == 'wcat' else ted(isbn)
