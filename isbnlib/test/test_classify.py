# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""nose tests for classifiers."""

from nose.tools import assert_equals
from .._oclc import query_classify as query


# this is a slow service

q1 = query('9781118241257') or {}
q2 = query('9780425284629') or {}



def test_query():
    """Test the query of classifiers (oclc.org) with 'low level' queries."""
    assert_equals(len(repr(query('9782253112105'))) > 10, True)
    assert_equals(len(repr(q1)) > 10, True)
    assert_equals(len(repr(q2)) > 10, True)


def test_query_no_data():
    """Test the query of classifiers (oclc.org) with 'low level' queries (no data)."""
    assert_equals(len(repr(query('9781849692341'))) == 2, True)
    assert_equals(len(repr(query('9781849692343'))) == 2, True)


def test_query_exists_ddc():
    """Test exists 'DDC'."""
    assert_equals(len(repr(q1['ddc'])) > 2, True)
    assert_equals(len(repr(q2['ddc'])) > 2, True)


def test_query_exists_lcc():
    """Test exists 'LCC'."""
    assert_equals(len(repr(q1['lcc'])) > 2, True)
    assert_equals(len(repr(q2['lcc'])) > 2, True)


def test_query_fast():
    """Test exists 'fast' classifiers."""
    assert_equals(len(repr(q1['fast'])) > 10, True)
    assert_equals(len(repr(q2['fast'])) > 10, True)


def test_query_owi():
    """Test exists 'owi' classifiers."""
    assert_equals(len(repr(q1['owi'])) > 10, True)
    assert_equals(len(repr(q2['owi'])) > 10, True)


def test_query_oclc():
    """Test exists 'oclc' classifiers."""
    assert_equals(len(repr(q1['oclc'])) > 10, True)
    assert_equals(len(repr(q2['oclc'])) > 10, True)
