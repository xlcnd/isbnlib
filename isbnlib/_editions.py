# -*- coding: utf-8 -*-
"""Return editions for a given ISBN."""

import logging

from ._core import EAN13
from ._exceptions import NotRecognizedServiceError, NotValidISBNError
from ._openled import query as oed
from ._thinged import query as ted
from .dev import vias

PROVIDERS = ('any', 'merge', 'openl', 'thingl')
TRUEPROVIDERS = ('openl', 'thingl')  # <-- by priority
LOGGER = logging.getLogger(__name__)


# pylint: disable=broad-except
def fake_provider_any(isbn):
    """Fake provider 'any' service."""
    providers = {'openl': oed, 'thingl': ted}
    for provider in TRUEPROVIDERS:
        data = []
        try:
            data = providers[provider](isbn)
            if len(data) > 1:
                return data
            continue  # pragma: no cover
        except Exception:  # pragma: no cover
            LOGGER.error("Some error on editions 'any' service for %s (%s)!",
                         isbn, provider)
            continue
    return data  # pragma: no cover


# pylint: disable=broad-except
def fake_provider_merge(isbn):
    """Fake provider 'merge' service."""
    try:  # pragma: no cover
        named_tasks = (('openl', oed), ('thingl', ted))
        results = vias.parallel(named_tasks, isbn)
        odata = results.get('openl', [])
        tdata = results.get('thingl', [])
        data = list(set(odata + tdata))
        return data
    except Exception:  # pragma: no cover
        LOGGER.error("Some error on editions 'merge' service for %s!", isbn)
        return []


def editions(isbn, service='merge'):
    """Return the list of ISBNs of editions related with this ISBN."""
    isbn = EAN13(isbn)
    if not isbn:
        LOGGER.critical('%s is not a valid ISBN', isbn)
        raise NotValidISBNError(isbn)

    if service not in PROVIDERS:
        LOGGER.critical('%s is not a recognized editions provider', service)
        raise NotRecognizedServiceError(service)

    from .registry import metadata_cache
    cache = metadata_cache
    if cache is not None:  # <-- IMPORTANT
        key = 'ed' + isbn + service
        if key in cache:
            return cache[key]

    if service == 'merge':
        eds = fake_provider_merge(isbn)
    if service == 'any':
        eds = fake_provider_any(isbn)

    if service == 'openl':
        eds = oed(isbn)
    if service == 'thingl':
        eds = ted(isbn)

    if eds and cache is not None:
        cache[key] = eds
        return eds
    return eds if eds else []
