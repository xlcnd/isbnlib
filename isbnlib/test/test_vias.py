# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""
nose tests
"""

import os
import platform

from nose.tools import assert_equals

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
    if os.getenv('APPVEYOR', '') != '':
        return True
    if os.getenv('GITHUB_OS', '') == 'windows':
        return True
    if os.getenv('GITHUB_OS', '') == 'macOS':
        return True
    if platform.system() == 'Windows':
        return True
    if platform.system() == 'Darwin':
        return True
    named_tasks = (('task1', task1), ('task2', task2))
    results = vias.multi(named_tasks, 5)
    data1 = results.get('task1', 0)
    data2 = results.get('task2', 0)
    data = data1 + data2
    assert data == 5 * 5 + 5 + 5
