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
    """Test 'vias' several modes of operation."""
    if WINDOWS:
        # appveyor doesn't allow!
        return
    assert_equals(len(repr(merge.query('9780321534965', 'parallel'))) > 170, True)
    assert_equals(len(repr(merge.query('9780321534965', 'multi'))) > 170, True)
    assert_equals(len(repr(merge.query('9780321534965', 'serial'))) > 170, True)

    # test if the secondary cache (cache in vias) does clears... sequentially
    assert_equals(len(repr(merge.query('9788806219345', 'serial'))) < 20, True)
    assert_equals(len(repr(merge.query('9780321534965', 'serial'))) > 170, True)
    assert_equals(len(repr(merge.query('9788806219345', 'serial'))) < 20, True)
