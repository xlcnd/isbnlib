# -*- coding: utf-8 -*-
"""Registry for metadata services."""


import sys
from . import _wcat as wcat
from . import _goob as goob
from . import _merge as merge
from . import _openl as openl
from . import _isbndb as isbndb
from ._imcache import IMCache
from ._exceptions import PluginNotLoadedError


# SERVICES

services = {'default': merge.query,
            'wcat': wcat.query,
            'goob': goob.query,
            'merge': merge.query,
            'openl': openl.query,
            'isbndb': isbndb.query
            }


def setdefaultservice(name):          # pragma: no cover
    """Set the default service."""
    global services
    services['default'] = services[name]


def add_service(name, query):         # pragma: no cover
    """Add a new service to services."""
    global services
    services[name] = query


# CACHE
# if you want a persistant cache you could use
# .dev.helpers ShelveCache(pathtofile)

metadata_cache = IMCache()            # should be an instance


def set_cache(cache):                 # pragma: no cover
    """Set cache for metadata."""
    global metadata_cache
    metadata_cache = cache
