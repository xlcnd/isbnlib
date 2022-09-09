# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file

import pytest

from ..registry import setdefaultbibformatter, setdefaultservice


# tests
def test_setdefaultbibformatter():
    """Test setdefaultbibformatter."""
    assert setdefaultbibformatter('json') == None
    with pytest.raises(Exception):
        setdefaultbibformatter('default')
    with pytest.raises(Exception):
        setdefaultbibformatter('')
    with pytest.raises(Exception):
        setdefaultbibformatter('xxx')


def test_setdefaultservice():
    """Test setdefaultservice."""
    assert setdefaultservice('goob') == None
    with pytest.raises(Exception):
        setdefaultservice('default')
    with pytest.raises(Exception):
        setdefaultservice('')
    with pytest.raises(Exception):
        setdefaultservice('xxx')
