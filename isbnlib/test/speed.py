# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""Crud Timer for 'import isbnlib'."""

import time

t = time.process_time()
import isbnlib
elapsed_time = time.process_time() - t
print(elapsed_time)
assert elapsed_time < 0.1
