# -*- coding: utf-8 -*-
"""Return editions for a given ISBN."""

import logging

from ._core import EAN13, to_isbn13
from ._exceptions import NotRecognizedServiceError, NotValidISBNError
from ._openled import query as _oed
from ._thinged import query as _ted
from ._wikied import query as _wiki
from .dev import cache, vias

PROVIDERS = ('any', 'merge', 'openl', 'thingl', 'wiki')
LOGGER = logging.getLogger(__name__)


# pylint: disable=broad-except
def _fake_provider_any(isbn):
    """Fake provider 'any' service."""
    providers = {'wiki': _wiki, 'openl': _oed, 'thingl': _ted}
    for provider in providers:
        try:
            data = providers[provider](isbn)
            if len(data) > 1:
                return list(data)
        except Exception:  # pragma: no cover
            LOGGER.error("Some error on editions 'any' service for %s (%s)!",
                         isbn, provider)
        continue  # pragma: no cover
    return [isbn]  # pragma: no cover


# pylint: disable=broad-except
def _fake_provider_merge(isbn):
    """Fake provider 'merge' service."""
    try:  # pragma: no cover
        named_tasks = (('openl', _oed), ('thingl', _ted), ('wiki', _wiki))
        results = vias.parallel(named_tasks, isbn)
        odata = results.get('openl', set())
        tdata = results.get('thingl', set())
        wdata = results.get('wiki', set())
        return list(odata | tdata | wdata)
    except Exception:  # pragma: no cover
        LOGGER.error("Some error on editions 'merge' service for %s!", isbn)
        return [isbn]


@cache
def get_editions(isbn, service):
    """Select the provider."""
    if service == 'merge':
        eds = _fake_provider_merge(isbn)
    if service == 'any':
        eds = _fake_provider_any(isbn)
    if service == 'openl':
        eds = list(_oed(isbn))
    if service == 'thingl':
        eds = list(_ted(isbn))
    if service == 'wiki':
        eds = list(_wiki(isbn))
    return list(set(map(to_isbn13, eds))) if eds else []


def editions(isbn, service='merge'):
    """Return the list of ISBNs of editions related with this ISBN."""
    isbn = EAN13(isbn)
    if not isbn:
        LOGGER.critical('%s is not a valid ISBN', isbn)
        raise NotValidISBNError(isbn)

    if service not in PROVIDERS:
        LOGGER.critical('%s is not a recognized editions provider', service)
        raise NotRecognizedServiceError(service)

    return get_editions(isbn, service)
