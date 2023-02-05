# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
""" tests for wikipedia."""
import pytest

from .._metadata import query

pytestmark = pytest.mark.network

def test_query():
    """Test 'wiki' metadata service."""
    # test query from metadata
    assert (len(repr(query('9780195132861', 'wiki'))) > 100) == True
    assert (len(repr(query('9780375869020', 'wiki'))) > 100) == True
    data = query('9780596003302', 'wiki')
    assert (len(repr(data['Authors'])) > 5) == True
    assert (len(repr(data['Publisher'])) > 5) == True
