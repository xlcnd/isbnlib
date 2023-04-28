# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""
tests
"""

from ..dev._fmt import _fmtbib

canonical = {
    'ISBN-13': '9780123456789',
    'Title': 'A book about nothing',
    'Publisher': 'No Paper Press',
    'Year': '2000',
    'Language': 'en',
    'Authors': ['John Smith', 'José Silva'],
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
