#!/usr/bin/env python
# -*- coding: utf-8 -*-


from .._infogroup import infogroup
from .._ext import info
from nose.tools import assert_equals, assert_raises


# nose tests
def test_infogroup():
    assert_equals(infogroup('9789720404427'), 'Portugal')
    assert_equals(infogroup('7204044271'), 'China')
    assert_equals(infogroup('9524712946'), 'Finland')
    assert_equals(infogroup('0330284983'),
                  'English - (UK, US, Australia, NZ, Canada, South Africa, Zimbabwe) (Ireland, Puerto Rico, Swaziland)')
    assert_equals(infogroup('3796519008'),
                  'German (Germany, Austria, Switzerland)')
    assert_equals(infogroup('92xxxxxxxxxxx'), None)
    assert_raises(Exception, infogroup, '')
    assert_equals(infogroup('9791090636071'), 'France')

def test_ext_info():
    assert_equals(info('9524712946'), 'Finland')
    assert_raises(Exception, info, '')

# flake8: noqa
