# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""
tests
"""

from .. import _goom as goom


def test_goom():
    """Test the Google's Multiple Books service."""
    assert (len(repr(goom.query('the old man and the sea'))) > 500) == True
    assert (len(repr(goom.query('plato republic'))) > 500) == True
