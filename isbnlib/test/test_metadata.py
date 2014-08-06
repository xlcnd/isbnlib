#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file

"""nose tests for metadata."""

from random import randrange
from .._metadata import query
from .._ext import meta
from nose.tools import assert_equals, assert_raises


def test_query():
    # test query from metadata
    assert_raises(Exception, query, '9781849692341', 'goog')
    assert_equals(len(repr(query('9781849692342', 'goob'))) > 150, True)
    assert_raises(Exception, query, '9781849692341', 'wcat')
    assert_equals(len(repr(query('9780321534965', 'wcat'))) > 150, True)
    assert_equals(len(repr(query('9780321534965'))) > 150, True)
    assert_equals(len(repr(query('9780321534965', 'merge'))) > 150, True)
    assert_equals(len(repr(query('9780321534965', 'goob'))) > 150, True)
    assert_equals(len(repr(query('9789934015960'))) > 150, True)
    assert_equals(len(repr(query('9781118241257'))) > 149, True)
    assert_raises(Exception, query, '9780000000', 'wcat', None)
    assert_raises(Exception, query, randrange(0, 1000000), 'wcat')


def test_ext_meta():
    # test meta from core
    assert_equals(len(repr(meta('9781849692342', 'goob'))) > 150, True)
    assert_equals(len(repr(meta('9780321534965', 'wcat'))) > 150, True)
    assert_equals(len(repr(meta('9780321534965', 'merge'))) > 150, True)
    assert_equals(len(repr(meta('9780321534965'))) > 150, True)
    assert_raises(Exception, meta, '9780000000', 'wcat', None)
    assert_raises(Exception, meta, randrange(0, 1000000), 'wcat')
