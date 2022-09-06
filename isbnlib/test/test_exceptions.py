# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""tests for Exceptions."""

import pytest

from .. import ISBNLibException
from .._ext import meta


def test_catchall():
    """Test the 'catch all' exception (ISBNLibException)."""
    with pytest.raises(Exception):
        meta('9781849692343', 'goob', None)

    def f1():
        try:
            meta('9781849692343')
        except ISBNLibException as ex:
            return str(ex.message)

    assert f1() == '(9781849692343) is not a valid ISBN'

    def f2():
        try:
            meta('9789720049612', 'xxx')
        except ISBNLibException as ex:
            return str(ex.message)

    assert f2() == '(xxx) is not a recognized service'


# NOTE the tests for other Exceptions are spread in the other tests
