# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""nose tests"""

from nose.tools import assert_equals, assert_raises

from .._isbn import Isbn


isbn=Isbn('9781250158062')


def test_ean13():
    """Test the 'Isbn class' for ean13."""
    assert_equals(isbn.ean13, '9781250158062')

def test_isbn13():
    """Test the 'Isbn class' for isbn13."""
    assert_equals(isbn.isbn13, '978-1-250-15806-2')

def test_isbn10():
    """Test the 'Isbn class' for isbn10."""
    assert_equals(isbn.isbn10, '1-250-15806-0')

def test_doi():
    """Test the 'Isbn class' for doi."""
    assert_equals(isbn.doi, '10.978.1250/158062')

def test_issued():
    """Test the 'Isbn class' for 'info'."""
    assert_equals(isbn.issued, True)

def test_info():
    """Test the 'Isbn class' for 'issued'."""
    assert_equals(isbn.info, 'English language')

def test_errors():
    """Test the 'Isbn class' for 'bad isbn'."""
    assert_raises(Exception, Isbn, '781250158062')

def test_str():
    """Test the 'Isbn class' for 'str'."""
    assert_equals(len(str(isbn)) > 20,  True)

def test_repr():
    """Test the 'Isbn class' for 'repr'."""
    assert_equals(len(repr(isbn)) > 20,  True)





