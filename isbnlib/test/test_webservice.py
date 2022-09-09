# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""
tests
"""

from ..dev.webservice import query as wsquery


def test_webservice():
    """Test that values can be passed to a WebService query."""
    assert (
        (len(repr(wsquery('http://example.org', values={'some': 'values'}))) > 0) == True)
