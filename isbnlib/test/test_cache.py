# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""Tests for the cache."""

from .._imcache import IMCache

cache = IMCache()


def setup_module():
    cache['123'] = 'abc'  #  <-- set


def teardown_module():
    del cache['123']


def test_cache_set():
    """Test 'cache' operations (set)."""
    cache['567'] = 'jkl'
    assert ('jkl' == cache['567']) == True


def test_cache_get():
    """Test 'cache' operations (get)."""
    assert cache.get('123') == cache['123']
    assert cache.get('000') == None
    assert cache.get('000', '') == ''


def test_cache_contains():
    """Test 'cache' operations (contains)."""
    assert ('123' in cache) == True


def test_cache_del():
    """Test 'cache' operations (del)."""
    cache['567'] = 'jkl'
    del cache['567']
    assert ('567' not in cache) == True
