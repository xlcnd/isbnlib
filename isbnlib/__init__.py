# -*- coding: utf-8 -*-
# flake8: noqa
# isort:skip_file
"""Library to validate, clean, transform and get metadata of ISBN strings (for devs)."""

# Define isbnlib API and set lib environment

import logging as _logging

from ._exceptions import (
    ISBNLibException,
    NotRecognizedServiceError,
    NotValidDefaultFormatterError,
    NotValidDefaultServiceError,
    NotValidISBNError,
    PluginNotLoadedError,
    quiet_errors,
)

# main modules
from ._core import (
    canonical,
    check_digit10,
    check_digit13,
    clean,
    EAN13,
    get_canonical_isbn,
    get_isbnlike,
    GTIN13,
    is_isbn10,
    is_isbn13,
    notisbn,
    RE_ISBN10,
    RE_ISBN13,
    RE_LOOSE,
    RE_NORMAL,
    RE_STRICT,
    to_isbn10,
    to_isbn13,
)
from ._doitotex import doi2tex
from ._ext import (
    cover,
    desc,
    doi,
    editions,
    info,
    isbn_from_words,
    mask,
    meta,
    ren,
)
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
    'canonical',
    'check_digit10',
    'check_digit13',
    'classify',
    'clean',
    'cover',
    'desc',
    'doi',
    'doi2tex',
    'ean13',
    'EAN13',
    'editions',
    'get_canonical_isbn',
    'get_isbnlike',
    'goom',
    'GTIN13',
    'info',
    'Isbn',
    'ISBN13',
    'isbn_from_words',
    'ISBNLibException',
    'is_isbn10',
    'is_isbn13',
    'mask',
    'meta',
    'notisbn',
    'NotRecognizedServiceError',
    'NotValidDefaultFormatterError',
    'NotValidDefaultServiceError',
    'NotValidISBNError',
    'PluginNotLoadedError',
    'quiet_errors',
    'RDDATE',
    'ren',
    'to_isbn10',
    'to_isbn13',
    '__support__',
    '__version__',
)

__version__ = '3.10.4'
__support__ = 'py27, py35, py36, py37, py38, pypy, pypy3'
