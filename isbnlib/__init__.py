# -*- coding: utf-8 -*-
# flake8: noqa
# isort:skip_file

"""Define isbnlib API and set lib environment."""

import logging as _logging

from ._exceptions import (quiet_errors, ISBNLibException,
                          NotRecognizedServiceError,
                          NotValidISBNError,
                          PluginNotLoadedError)

# config _logging for lib (NullHandler not available for py26)
try:
    _nh = _logging.NullHandler()
except:              # pragma: no cover
    class NullHandler(_logging.Handler):
        def emit(self, record):
            pass
    _nh = NullHandler()
_logging.getLogger('isbnlib').addHandler(_nh)

# configuration
from . import config                                # <-- first import

# main modules
from ._core import (is_isbn10, is_isbn13, to_isbn10, to_isbn13, clean,
                    canonical, notisbn, get_isbnlike, get_canonical_isbn,
                    EAN13)
from ._ext import (cover, desc, mask, meta, info, editions, isbn_from_words,
                   doi, ren)
from ._goom import query as goom
from ._doitotex import doi2tex

# Ranges Database date
from ._data.data4mask import RDDATE

# alias
ISBN13 = EAN13
ean13 = EAN13

# dunders

__all__ = ('is_isbn10', 'is_isbn13', 'clean', 'mask', 'info', 'meta',
           'to_isbn10', 'to_isbn13', 'get_isbnlike', 'notisbn',
           'ean13', 'EAN13', 'cover', 'desc',
           'canonical', 'get_canonical_isbn', 'editions', 'isbn_from_words',
           'quiet_errors', 'config', '__version__', '__support__',
           'doi', 'ren', 'ISBN13', 'ISBNLibException',
           'NotRecognizedServiceError', 'NotValidISBNError',
           'PluginNotLoadedError', 'goom', 'doi2tex', 'RDDATE')

__version__ = '3.5.6'                               # <-- literal IDs
__support__ = 'py26, py27, py33, py34, pypy'        # <-- literal IDs
