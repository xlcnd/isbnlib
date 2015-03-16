# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file

from nose.tools import assert_equals, raises

from .._exceptions import NotRecognizedServiceError, NotValidISBNError
from .._ext import editions


# nose tests


def test_editions1():
    """Test the 'editions' service."""
    assert_equals(len(editions('9780156001311', service='wcat')) > 19, True)
    assert_equals(len(editions('9780151446476', service='thingl')) > 19, True)
    assert_equals(len(editions('9780151446476', service='any')) > 19, True)
    assert_equals(len(editions('9780151446476', service='merge')) > 19, True)


@raises(NotValidISBNError)
def test_editions2():
    """Test the 'editions' service error detection (NotValidISBNError)."""
    editions('978')


@raises(NotRecognizedServiceError)
def test_editions3():
    """Test the 'editions' service error detection (NotRecognizedServiceError)."""
    editions('9780156001311', service='xxx')
