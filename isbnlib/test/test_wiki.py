# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
""" nose tests for wikipedia."""

from nose.tools import assert_equals

from .._metadata import query


def test_query():
    """Test 'wiki' metadata service."""
    # test query from metadata
    assert_equals(len(repr(query('9780195132861', 'wiki'))) > 100, True)
    assert_equals(len(repr(query('9780156001311', 'wiki'))) > 100, True)
