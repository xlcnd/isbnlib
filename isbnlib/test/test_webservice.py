# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""
nose tests
"""

from nose.tools import assert_equals

from ..dev.webservice import query as wsquery


def test_webservice():
    """Test that values can be passed to a WebService query."""
    assert_equals(
        len(repr(wsquery(
                         'http://example.org',
                         values={'some': 'values'}
                         ))) > 0, True)
