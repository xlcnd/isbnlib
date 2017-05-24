# -*- coding: utf-8 -*-
# flake8: noqa
# isort:skip_file
"""Library to validate, clean, transform and get metadata of ISBN strings (for devs)."""

# Define isbnlib API and set lib environment

import logging as _logging

from ._exceptions import (quiet_errors, ISBNLibException,
                          NotRecognizedServiceError, NotValidISBNError,
                          PluginNotLoadedError)

# config _logging for lib (NullHandler not available for py26)
try:
    _nh = _logging.NullHandler()
except:  # pragma: no cover

    class NullHandler(_logging.Handler):
        def emit(self, record):
            pass

    _nh = NullHandler()
_logging.getLogger('isbnlib').addHandler(_nh)

# configuration
from . import config  # <-- first import

# main modules
from ._core import (is_isbn10, is_isbn13, to_isbn10, to_isbn13, check_digit10,
                    check_digit13, clean, canonical, notisbn, get_isbnlike,
                    get_canonical_isbn, GTIN13, EAN13, RE_ISBN10, RE_ISBN13,
                    RE_LOOSE, RE_NORMAL, RE_STRICT)
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

__all__ = ('is_isbn10', 'is_isbn13', 'clean', 'check_digit10', 'check_digit13',
           'mask', 'info', 'meta', 'to_isbn10', 'to_isbn13', 'get_isbnlike',
           'notisbn', 'ean13', 'EAN13', 'cover', 'desc', 'canonical',
           'get_canonical_isbn', 'editions', 'isbn_from_words', 'quiet_errors',
           'config', '__version__', '__support__', 'doi', 'ren', 'ISBN13',
           'GTIN13', 'ISBNLibException', 'NotRecognizedServiceError',
           'NotValidISBNError', 'PluginNotLoadedError', 'goom', 'doi2tex',
           'RDDATE')

__version__ = '3.7.2'  # <-- literal IDs
__support__ = 'py26, py27, py33, py34, py35, pypy, pypy3'  # <-- literal IDs
