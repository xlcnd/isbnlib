# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""tests"""

import pytest

from .._isbn import Isbn

isbn=Isbn('9781250158062')


def test_ean13():
    """Test the 'Isbn class' for ean13."""
    assert isbn.ean13 == '9781250158062'

def test_isbn13():
    """Test the 'Isbn class' for isbn13."""
    assert isbn.isbn13 == '978-1-250-15806-2'

def test_isbn10():
    """Test the 'Isbn class' for isbn10."""
    assert isbn.isbn10 == '1-250-15806-0'

def test_doi():
    """Test the 'Isbn class' for doi."""
    assert isbn.doi == '10.978.1250/158062'

def test_issued():
    """Test the 'Isbn class' for 'issued'."""
    assert isbn.issued == True
    isbn2=Isbn('9786610326266')
    assert isbn2.issued == False

def test_info():
    """Test the 'Isbn class' for 'info'."""
    assert isbn.info == 'English language'

def test_errors():
    """Test the 'Isbn class' for 'bad isbn'."""
    with pytest.raises(Exception):
        Isbn('781250158062')

def test_str():
    """Test the 'Isbn class' for 'str'."""
    assert (len(str(isbn)) > 20) ==  True

def test_repr():
    """Test the 'Isbn class' for 'repr'."""
    assert (len(repr(isbn)) > 20) ==  True
