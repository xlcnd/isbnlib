# -*- coding: utf-8 -*-
"""Registry for metadata services, formatters and cache."""

import logging

from pkg_resources import iter_entry_points

from . import _goob as goob
from . import _openl as openl
from . import _wiki as wiki
from . import NotValidDefaultServiceError
from . import NotValidDefaultFormatterError
from ._imcache import IMCache
from .config import options
from .dev._fmt import _fmtbib

LOGGER = logging.getLogger(__name__)

# SERVICES

services = {
    'default': goob.query,
    'goob': goob.query,
    'openl': openl.query,
    'wiki': wiki.query,
}

PROVIDERS = ()


def setdefaultservice(name):
    """Set the default service."""
    global services
    services['default'] = services[name.lower()]
    if name != 'default' and name in services:
        services['default'] = services[name.lower()]
    else:
        LOGGER.critical('Wrong default service')
        raise NotValidDefaultServiceError(name)


def add_service(name, query):  # pragma: no cover
    """Add a new service to services."""
    global services
    services[name.lower()] = query


# FORMATTERS

bibformatters = {
    'default': lambda x: _fmtbib('labels', x),
    'labels': lambda x: _fmtbib('labels', x),
    'bibtex': lambda x: _fmtbib('bibtex', x),
    'csl': lambda x: _fmtbib('csl', x),
    'json': lambda x: _fmtbib('json', x),
    'opf': lambda x: _fmtbib('opf', x),
    'endnote': lambda x: _fmtbib('endnote', x),
    'ris': lambda x: _fmtbib('ris', x),
    'refworks': lambda x: _fmtbib('ris', x),
    'msword': lambda x: _fmtbib('msword', x),
}  # pragma: no cover

BIBFORMATS = ()


def setdefaultbibformatter(name):
    """Set the default formatter."""
    global bibformatters
    if name != 'default' and name in bibformatters:
        bibformatters['default'] = bibformatters[name.lower()]
    else:
        LOGGER.critical('Wrong default bibformatter')
        raise NotValidDefaultFormatterError(name)


def add_bibformatter(name, formatter):  # pragma: no cover
    """Add a new formatter to formatters."""
    global bibformatters
    bibformatters[name] = formatter.lower()


# pylint: disable=broad-except
def load_plugins():  # pragma: no cover
    """Load plugins with groups: isbnlib.metadata & isbnlib.formatters."""
    # get metadata plugins from entry_points
    if options.get('LOAD_METADATA_PLUGINS', True):
        try:
            for entry in iter_entry_points(group='isbnlib.metadata'):
                add_service(entry.name, entry.load())
        except Exception:
            LOGGER.critical('Some metadata plugins were not loaded!')
    global PROVIDERS
    _buf = list(services.keys())
    _buf.remove('default')
    PROVIDERS = tuple(sorted(_buf))
    # get formatters from entry_points
    if options.get('LOAD_FORMATTER_PLUGINS', True):
        try:
            for entry in iter_entry_points(group='isbnlib.formatters'):
                add_bibformatter(entry.name, entry.load())
        except Exception:
            LOGGER.critical('Some formatters plugins were not loaded!')
    global BIBFORMATS
    _buf = list(bibformatters.keys())
    _buf.remove('labels')
    _buf.remove('default')
    BIBFORMATS = tuple(sorted(_buf))


# load plugins on import
load_plugins()
del load_plugins

# CACHE
metadata_cache = IMCache()  # should be an instance


def set_cache(cache):  # pragma: no cover
    """Set cache for metadata."""
    global metadata_cache
    metadata_cache = cache
