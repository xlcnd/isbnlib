# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file

try:
    from time import process_time as timer
except:  # for py2
    import timeit

    timer = timeit.default_timer

import pytest

from .._exceptions import NotRecognizedServiceError, NotValidISBNError
from .._ext import editions


def test_editions_openl():
    """Test the 'openl editions' service."""
    assert (len(editions('9780151446476', service='openl')) >= 1) == True


@pytest.mark.network
def test_editions_thingl():
    """Test the 'thingl editions' service."""
    assert (len(editions('9780151446476', service='thingl')) > 2) == True


@pytest.mark.network
def test_editions_wiki():
    """Test the 'wiki editions' service."""
    assert (len(editions('9780440414803', service='wiki')) > 5) == True


@pytest.mark.network
def test_editions_any():
    """Test the 'any editions' service."""
    assert (len(editions('9780151446476', service='any')) > 1) == True


@pytest.mark.network
def test_editions_merge():
    """Test the 'merge editions' service."""
    assert (len(editions('9780151446476', service='merge')) > 2) == True


def test_editions_NotValidISBNError():
    """Test the 'editions' service error detection (NotValidISBNError)."""
    with pytest.raises(NotValidISBNError):
        editions('978')


def test_editions_NotRecognizedServiceError():
    """Test the 'editions' service error detection (NotRecognizedServiceError)."""
    with pytest.raises(NotRecognizedServiceError):
        editions('9780156001311', service='xxx')


@pytest.mark.network
def test_cache():
    """Test the 'editions' cache."""
    t = timer()
    assert (len(editions('9780151446476', service='merge')) > 19) == True
    elapsed_time = timer() - t
    millis = int(elapsed_time * 1000)
    assert (millis < 100) == True
