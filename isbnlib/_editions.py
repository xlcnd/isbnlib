# -*- coding: utf-8 -*-
"""Return editions for a given ISBN."""

import logging

from ._core import EAN13
from ._exceptions import NotRecognizedServiceError, NotValidISBNError
from ._openled import query as oed
from ._thinged import query as ted
from ._wcated import query as wed

PROVIDERS = ('any', 'merge', 'openl', 'thingl', 'wcat')
TRUEPROVIDERS = ('wcat', 'openl', 'thingl')  # <-- by priority
LOGGER = logging.getLogger(__name__)


def fake_provider_any(isbn):
    """Fake provider 'any' service."""
    providers = {'wcat': wed, 'openl': oed, 'thingl': ted}
    for provider in TRUEPROVIDERS:
        data = []
        try:
            data = providers[provider](isbn)
            if len(data) > 1:
                return data
            continue  # pragma: no cover
        except:  # pragma: no cover
            continue
    return data  # pragma: no cover


def fake_provider_merge(isbn):
    """Fake provider 'merge' service."""
    data = []
    try:  # pragma: no cover
        wdata = wed(isbn)
        if not wdata:
            wdata = []
        odata = oed(isbn)
        if not odata:
            odata = []
        tdata = ted(isbn)
        if not tdata:
            tdata = []
        data = list(set(wdata + odata + tdata))
        return data
    except:  # pragma: no cover
        return data


def editions(isbn, service='merge'):
    """Return the list of ISBNs of editions related with this ISBN."""
    isbn = EAN13(isbn)
    if not isbn:
        LOGGER.critical('%s is not a valid ISBN', isbn)
        raise NotValidISBNError(isbn)

    if service not in PROVIDERS:
        LOGGER.critical('%s is not a recognized editions provider', service)
        raise NotRecognizedServiceError(service)

    if service == 'merge':
        return fake_provider_merge(isbn)
    if service == 'any':
        return fake_provider_any(isbn)

    if service == 'wcat':
        return wed(isbn)
    if service == 'openl':
        return oed(isbn)
    if service == 'thingl':
        return ted(isbn)
