# -*- coding: utf-8 -*-
# flake8: noqa
# isort:skip_file
"""Library to validate, clean, transform and get metadata of ISBN strings (for devs)."""

# Define isbnlib API and set lib environment

import logging as _logging

from ._exceptions import (
    quiet_errors,
    ISBNLibException,
    NotRecognizedServiceError,
    NotValidISBNError,
    NotValidDefaultServiceError,
    NotValidDefaultFormatterError,
    PluginNotLoadedError,
)

# main modules
from ._core import (
    check_digit10,
    check_digit13,
    clean,
    canonical,
    get_isbnlike,
    get_canonical_isbn,
    is_isbn10,
    is_isbn13,
    notisbn,
    to_isbn10,
    to_isbn13,
    EAN13,
    GTIN13,
    RE_ISBN10,
    RE_ISBN13,
    RE_LOOSE,
    RE_NORMAL,
    RE_STRICT,
)
from ._doitotex import doi2tex
from ._ext import cover, desc, mask, meta, info, editions, isbn_from_words, doi, ren
from ._goom import query as goom
from ._isbn import Isbn
from ._oclc import query_classify as classify

# Ranges Database date
from ._data.data4info import RDDATE

# config _logging for lib
_nh = _logging.NullHandler()
_logging.getLogger('isbnlib').addHandler(_nh)

# alias
ean13 = EAN13
ISBN13 = EAN13

# dunders
__all__ = (
    'is_isbn10',
    'is_isbn13',
    'clean',
    'check_digit10',
    'check_digit13',
    'mask',
    'info',
    'meta',
    'classify',
    'to_isbn10',
    'to_isbn13',
    'get_isbnlike',
    'notisbn',
    'ean13',
    'EAN13',
    'ISBN13',
    'GTIN13',
    'cover',
    'desc',
    'canonical',
    'get_canonical_isbn',
    'editions',
    'isbn_from_words',
    'goom',
    'doi',
    'doi2tex',
    'ren',
    'quiet_errors',
    '__version__',
    '__support__',
    'RDDATE',
    'Isbn',
    'ISBNLibException',
    'NotRecognizedServiceError',
    'NotValidISBNError',
    'NotValidDefaultFormatterError',
    'NotValidDefaultServiceError',
    'PluginNotLoadedError',
)

__version__ = '3.10.4'
__support__ = 'py27, py35, py36, py37, py38, pypy, pypy3'
