#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""
nose tests
"""

import os

from .. import _merge as merge
from nose.tools import assert_equals


WINDOWS = os.name == 'nt'


def test_vias():
    if WINDOWS:
        # appveyor doesn't allow!
        return
    assert_equals(len(repr(merge.query('9780321534965', 'parallel'))) in (173, 179), True)
    assert_equals(len(repr(merge.query('9780321534965', 'multi'))) in (173, 179), True)
    assert_equals(len(repr(merge.query('9780321534965', 'serial'))) in (173, 179), True)
