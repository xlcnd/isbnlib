# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""Tests for the cache."""


from nose.tools import assert_equals, assert_raises
from .._imcache import IMCache

cache = IMCache()


def setup_module():
    cache["123"] = 'abc'  #  <-- set


def teardown_module():
    del cache["123"]


def test_cache_set():
    """Test 'cache' operations (set)."""
    cache['567'] = 'jkl'
    assert_equals('jkl' == cache['567'], True)


def test_cache_get():
    """Test 'cache' operations (get)."""
    assert_equals(cache.get("123"), cache['123'])
    assert_equals(cache.get("000"), None)
    assert_equals(cache.get("000", ""), "")


def test_cache_contains():
    """Test 'cache' operations (contains)."""
    assert_equals("123" in cache, True)


def test_cache_del():
    """Test 'cache' operations (del)."""
    del cache['567']
    assert_equals("567" not in cache, True)
