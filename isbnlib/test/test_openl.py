#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa

""" nose tests
NEEDS isbntools installed!
"""
from .._metadata import query
from nose.tools import assert_equals, assert_raises


def test_query():
    # test query from metadata
    assert_equals(len(repr(query('9780195132861', 'openl'))) in (185, 191), True)
