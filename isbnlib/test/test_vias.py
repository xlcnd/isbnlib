# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""
tests
"""

import os
import platform

from ..dev import vias


def task1(arg):
    return arg * arg


def task2(arg):
    return arg + arg


def test_vias_serial():
    """Test 'vias' (serial)."""
    named_tasks = (('task1', task1), ('task2', task2))
    results = vias.serial(named_tasks, 5)
    data1 = results.get('task1', 0)
    data2 = results.get('task2', 0)
    data = data1 + data2
    assert data == 5 * 5 + 5 + 5


def test_vias_parallel():
    """Test 'vias' (parallel)."""
    named_tasks = (('task1', task1), ('task2', task2))
    results = vias.parallel(named_tasks, 5)
    data1 = results.get('task1', 0)
    data2 = results.get('task2', 0)
    data = data1 + data2
    assert data == 5 * 5 + 5 + 5


def test_vias_multi():
    """Test 'vias' (multi)."""
    # Is NOT allowed in Windows & macOS!
    if os.getenv('GITHUB_OS', '') in ('windows', 'macOS'):
        assert True
        return
    if platform.system() in ('Windows', 'Darwin'):
        assert True
        return
    named_tasks = (('task1', task1), ('task2', task2))
    results = vias.multi(named_tasks, 5)
    data1 = results.get('task1', 0)
    data2 = results.get('task2', 0)
    data = data1 + data2
    assert data == 5 * 5 + 5 + 5
