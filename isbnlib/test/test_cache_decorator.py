# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""Tests for the @cache."""

# TODO add more tests for other operations

from .. import classify, meta, registry

cache = registry.metadata_cache


def setup_module():
    meta('9780375869020')  #  <-- set
    classify('9781118241257')  #  <-- set


def teardown_module():
    del cache["query('9780375869020', 'default'){}"]


def test_cache_meta():
    """Test '@cache' meta."""
    assert (
        (len(repr(cache.get("query('9780375869020', 'default'){}"))) > 100) == True)
    assert (
        len(repr(cache.get("query('9780375869020', 'default'){}"))) ==
        len(repr(cache["query('9780375869020', 'default'){}"])))


# def test_cache_classify():
#    """Test '@cache' classify."""
#    assert_equals(len(repr(cache.get("query_classify('9781118241257',){}"))) > 5, True)
#    assert_equals(
#        len(repr(cache.get("query_classify('9781118241257',){}"))),
#        len(repr(cache["query_classify('9781118241257',){}"])),
#    )
