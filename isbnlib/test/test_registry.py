# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file

from nose.tools import assert_raises

from ..registry import setdefaultbibformatter, setdefaultservice


def test_setdefaultbibformatter():
    """Test setdefaultbibformatter."""
    assert setdefaultbibformatter('json') == None
    assert_raises(Exception, setdefaultbibformatter, 'default')
    assert_raises(Exception, setdefaultbibformatter, '')
    assert_raises(Exception, setdefaultbibformatter, 'xxx')


def test_setdefaultservice():
    """Test setdefaultservice."""
    assert setdefaultservice('goob') == None
    assert_raises(Exception, setdefaultservice, 'default')
    assert_raises(Exception, setdefaultservice, '')
    assert_raises(Exception, setdefaultservice, 'xxx')
