# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""
nose tests
"""

from ..dev._helpers import last_first, cutoff_tokens, parse_placeholders
from nose.tools import assert_equals


def test_last_first():
    assert_equals(last_first("Surname, First Name"), {"last": "Surname", "first": "First Name"})
    assert_equals(last_first("First Name Surname"), {"last": "Surname", "first": "First Name"})
    assert_equals(last_first("Surname1, First1 and Sur2, First2"), {"last": "Surname1", "first": "First1 and Sur2, First2"})


def test_cutoff_tokens():
    assert_equals(cutoff_tokens(['1', '23', '456'], 3), ['1', '23'])


def test_parse_placeholders():
    assert_equals(parse_placeholders('{isbn}_akaj_{name}'), ['{isbn}', '{name}'])
    
