# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file

from nose.tools import assert_equals, assert_raises

from .._ext import info
from .._infogroup import infogroup


# nose tests
def test_infogroup():
    """Test 'infogroup' language/country function."""
    assert infogroup('9789727576807') == 'Portugal'
    assert infogroup('978-972-757-680-7') == 'Portugal'
    assert infogroup('7500117019') == "China, People's Republic"
    assert infogroup('7-5001-1701-9') == "China, People's Republic"
    assert infogroup('9524712946') == 'Finland'
    assert infogroup('0330284983') == 'English language'
    assert infogroup('3796519008') == 'German language'
    assert_raises(Exception, infogroup, '92xxxxxxxxxxx')
    assert_raises(Exception, infogroup, '')
    assert infogroup('9791090636071') == 'France'
    assert infogroup('9786131796364') == 'Mauritius'
    assert infogroup('9789992158104') == 'Qatar'


def test_ext_info():
    """Test 'info' language/country function."""
    assert info('9524712946') == 'Finland'
    assert_raises(Exception, info, '')


def test_ext_info():
    """Test 'info' not issued ISBN."""
    assert info('9789999999991') == ''
