# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file

from random import randrange

from nose.tools import assert_raises

from .._ext import meta
from .._metadata import query


def test_query():
    """Test the query of metadata with 'low level' queries."""
    # test query from metadata
    assert_raises(Exception, query, '9781849692341', 'goog')
    assert_raises(Exception, query, '9781849692343', 'goob')
    # assert_equals(query('9789934015960', 'goob'), {})
    assert (len(repr(query('9780321534965'))) > 100) == True
    assert (len(repr(query('9780321534965', 'goob'))) > 100) == True
    # assert_equals(len(repr(query('9789934015960'))) > 100, True)
    assert (len(repr(query(u'9781118241257'))) > 100) == True
    assert_raises(Exception, query, '9780000000', 'goob')
    assert_raises(Exception, query, randrange(0, 1000000), 'goob')


def test_ext_meta():
    """Test the query of metadata with 'high level' meta function."""
    # test meta from core
    assert (len(repr(meta('9780321534965', 'goob'))) > 100) == True
    assert (len(repr(meta('9780321534965'))) > 100) == True
    assert_raises(Exception, meta, '9780000000', 'goob')
    assert_raises(Exception, meta, randrange(0, 1000000), 'goob')
    assert_raises(Exception, meta, '9781849692343', 'goob')
