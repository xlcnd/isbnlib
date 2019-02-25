# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""Crude Timer for 'import isbnlib'."""

import time

t = time.process_time()
import isbnlib
elapsed_time = time.process_time() - t
millis = int(elapsed_time * 1000)
print("{} milliseconds < 100 milliseconds".format(millis))
assert elapsed_time < 100
