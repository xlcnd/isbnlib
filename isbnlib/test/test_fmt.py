# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""
nose tests
"""

from nose.tools import assert_equals

from ..dev._bouth23 import u
from ..dev._fmt import _fmtbib

canonical = {
    'ISBN-13': u('9780123456789'),
    'Title': u('A book about nothing'),
    'Publisher': u('No Paper Press'),
    'Year': u('2000'),
    'Language': u('en'),
    'Authors': [u('John Smith'), u('José Silva')],
}


def test_fmtbib():
    """Test the formatting into several bibliographic formats."""
    assert len(_fmtbib('bibtex', canonical)) == 182
    assert len(_fmtbib('labels', canonical)) == 158
    assert len(_fmtbib('endnote', canonical)) == 103
    assert len(_fmtbib('msword', canonical)) == 485
    assert len(_fmtbib('json', canonical)) == 229
    assert len(_fmtbib('csl', canonical)) == 253
    assert len(_fmtbib('csv', canonical)) == 94
    assert len(_fmtbib('ris', canonical)) == 130
    assert len(_fmtbib('opf', canonical)) == 861
