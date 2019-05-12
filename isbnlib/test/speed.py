# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""Crude Timer for 'import isbnlib'."""

import time

print("Test 'import speed' of:")


def speed_isbnlib():
    """Test import speed of 'isbnlib'."""
    t = time.process_time()
    import isbnlib
    elapsed_time = time.process_time() - t
    millis = int(elapsed_time * 1000)
    print("(isbnlib)  {} milliseconds < 100 milliseconds".format(millis))
    assert millis < 100


def speed_registry():
    """Test import speed of 'registry'."""
    t = time.process_time()
    from isbnlib import registry
    elapsed_time = time.process_time() - t
    millis = int(elapsed_time * 1000)
    print("(registry) {} milliseconds < 100 milliseconds".format(millis))
    assert millis < 100


speed_isbnlib()
speed_registry()
