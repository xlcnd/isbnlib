# -*- coding: utf-8 -*-
# flake8:noqa
# pylint: skip-file
"""Expose useful features."""

from .._imcache import IMCache
from ._files import File, cwdfiles
from ._fmt import _fmtbib, _fmts
from ._helpers import (
    cutoff_tokens,
    fake_isbn,
    last_first,
    normalize_space,
    parse_placeholders,
)

# alias (to keep backwards compatibility)
fmtbib = _fmtbib
fmts = _fmts

__all__ = [
    'File',
    'IMCache',
    'cutoff_tokens',
    'cwdfiles',
    'fmtbib',
    'fmts',
    'last_first',
    'normalize_space',
    'parse_placeholders',
    'fake_isbn',
]
