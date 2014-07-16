# -*- coding: utf-8 -*-

"""Define isbntools API and set lib environment."""

__all__ = ('is_isbn10', 'is_isbn13', 'clean', 'mask', 'info', 'meta',
           'to_isbn10', 'to_isbn13', 'get_isbnlike', 'notisbn', 'EAN13',
           'canonical', 'get_canonical_isbn', 'editions', 'isbn_from_words',
           'quiet_errors', 'config', '__version__', '__support__',
           'doi', 'ren', 'ISBN13', 'ISBNToolsException', 'ISBNLibException',
           'NotRecognizedServiceError', 'NotValidISBNError',
           'PluginNotLoadedError', 'goom', 'doi2tex')

__version__ = '3.4.2'                               # <-- literal IDs
__support__ = 'py26, py27, py33, py34, pypy'        # <-- literal IDs

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
from ._ext import (mask, meta, info, editions, isbn_from_words, doi, ren)
from ._goom import query as goom
from ._doitotex import doi2tex

# alias
ISBN13 = EAN13
ISBNToolsException = ISBNLibException
