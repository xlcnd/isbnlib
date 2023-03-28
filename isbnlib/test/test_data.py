# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""tests"""

import pytest

from ..dev import Metadata, stdmeta


def test_stdmeta():
    """Test the transformation of raw records into standard metadata."""
    # test stdmeta from data
    r = {
        'ISBN-13': '9780123456789 ',
        'Title': 'Bla. Bla /Title .',
        'Publisher': '',
        'Year': '2000',
        'Language': 'en',
        'Authors': ['author1. mba', 'author2   '],
    }
    R = {
        'ISBN-13': '9780123456789',
        'Title': 'Bla. Bla /Title',
        'Publisher': '',
        'Year': '2000',
        'Language': 'en',
        'Authors': ['author1. mba', 'author2'],
    }
    A = {
        'ISBN-13': '9780123456789 ',
        'Title': b'Bla. Bla /Title .',
        'Publisher': '',
        'Year': b'2000',
        'Language': 'en',
        'Authors': ['author1. mba', 'author2   '],
    }
    B = {
        'ISBN-13': '9780123456789',
        'Title': 'Bla. Bla /Title .',
        'Publisher': '',
        'Year': '2000',
        'Language': 'en',
        'Authors': 'author1',
    }
    assert stdmeta(r) == R
    assert stdmeta(R) == R
    with pytest.raises(Exception):
        stdmeta(A)
    with pytest.raises(Exception):
        stdmeta(B)


def test_metaclass():
    """Test the creation of a Metadata class from raw records."""
    R = {
        'ISBN-13': '9780123456789',
        'Title': 'Bla. Bla /Title',
        'Publisher': '',
        'Year': '2000',
        'Language': 'en',
        'Authors': ['author1. mba', 'author2'],
    }
    dt = Metadata(R)
    assert dt.value == R


def test_metrge():
    """Test the merging of records."""
    R = {
        'ISBN-13': '9780123456789',
        'Title': 'Bla. Bla /Title',
        'Publisher': '',
        'Year': '2000',
        'Language': 'en',
        'Authors': ['author1. mba', 'author2'],
    }
    T = {
        'ISBN-13': '9780123456789',
        'Title': 'Bla. Bla /Title',
        'Publisher': 'Pub House',
        'Year': '2000',
        'Language': 'en',
        'Authors': ['author1. mba', 'author2'],
    }
    dt = Metadata(R)
    dt.merge(T)
    assert dt.value == T
