# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
""" nose tests
"""

from nose.tools import assert_equals, assert_raises

from .._metadata import query


def test_query():
    """Test 'openl' metadata service."""
    # test query from metadata
    assert_equals(len(repr(query('9780195132861', 'openl'))) > 140, True)
    assert_equals(len(repr(query('9780156001311', 'openl'))) > 140, True)
