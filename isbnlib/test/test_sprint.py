# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file

import os
import sys

from nose.tools import assert_equals

from ..dev.bouth23 import b
from ..dev.helpers import sprint
from .adapters import run_code

"""
nose tests
"""

WINDOWS = os.name == 'nt'

def test_sprint():
    code = "from isbnlib.dev.bouth23 import u;from isbnlib.dev.helpers import sprint;sprint(u('abc'))"
    if WINDOWS:
        assert_equals(run_code(code), b('abc\r\n'))
    else:
        assert_equals(run_code(code), b('abc\n'))
