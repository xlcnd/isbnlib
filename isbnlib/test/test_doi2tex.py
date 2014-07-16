#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa
"""
nose tests
"""

from .. import doi2tex
from nose.tools import assert_equals


def test_doi2tex():
    assert_equals(len(repr(doi2tex('10.2139/ssrn.2411669'))) > 50, True)
