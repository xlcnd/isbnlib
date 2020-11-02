# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""
nose tests
"""

from nose.tools import assert_equals

from .. import doi2tex

from ..config import options


def setup_module():
    # this is a slow service
    options.set_option('URLOPEN_TIMEOUT', 25)


def teardown_module():
    # reset URLOPEN_TIMEOUT to default value
    options.set_option('URLOPEN_TIMEOUT', 10)


def test_doi2tex():
    """Test the doi2tex service."""
    assert_equals(len(repr(doi2tex('10.2139/ssrn.2411669'))) > 50, True)
