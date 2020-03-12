# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""
nose tests
"""

from nose.tools import assert_equals

from .. import _goom as goom


def test_goom():
    """Test the Google's Multiple Books service."""
    assert_equals(
        len(repr(goom.query('the old man and the sea'))) > 500, True)
    assert_equals(
        len(repr(goom.query('emergências obstréticas'))) > 500, True)
