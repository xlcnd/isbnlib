# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""Crude Timer for 'import isbnlib'."""

import sys
import time


def test_speed_isbnlib():
    """Test import speed of 'isbnlib'."""
    if sys.version < '3': return True
    t = time.process_time()
    import isbnlib

    elapsed_time = time.process_time() - t
    millis = int(elapsed_time * 1000)
    print('(isbnlib)  {} milliseconds < 100 milliseconds'.format(millis))
    assert millis < 100
    isbnlib.__version__


def test_speed_registry():
    """Test import speed of 'registry'."""
    if sys.version < '3': return True
    t = time.process_time()
    from isbnlib import registry

    elapsed_time = time.process_time() - t
    millis = int(elapsed_time * 1000)
    print('(registry) {} milliseconds < 135 milliseconds'.format(millis))
    assert millis < 135
    registry.BIBFORMATS
