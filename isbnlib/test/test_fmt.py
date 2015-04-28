# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file

"""
nose tests
"""

from nose.tools import assert_equals
from ..dev._bouth23 import u
from ..dev._fmt import fmtbib


canonical = {
             'ISBN-13': u('9780123456789'),
             'Title': u('A book about nothing'),
             'Publisher': u('No Paper Press'),
             'Year': u('2000'),
             'Language': u('en'),
             'Authors': [u('John Smith'), u('José Silva')]
             }

def test_fmtbib():
    """Test the formating into several bibliographic formats."""
    assert_equals(len(fmtbib("bibtex", canonical)), 182)
    assert_equals(len(fmtbib("labels", canonical)), 158)
    assert_equals(len(fmtbib("endnote", canonical)), 103)
    assert_equals(len(fmtbib("msword", canonical)), 485)
    assert_equals(len(fmtbib("json", canonical)), 229)
    assert_equals(len(fmtbib("refworks", canonical)), 130)
    assert_equals(len(fmtbib("opf", canonical)), 861)
