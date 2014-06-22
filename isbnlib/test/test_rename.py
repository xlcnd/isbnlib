#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file

import os
from nose.tools import assert_equals, assert_raises
from .._ext import ren
from ..dev.helpers import File, cwdfiles
from ..dev.bouth23 import u

"""
nose tests
"""


TESTFILE = '/tmp/海明威-deleteme.pdf'
NEW_BASENAME = '海明威-deleteme-PLEASE.pdf'

F1 = '9780321534965.pdf'
F2 = '9781597499644.pdf'
F3 = '9781852330729.pdf'
F4 = '9787500117018.pdf'
F5 = '9789727576807.pdf'

F6 = 'Campos2011_Emergências obstétricas_9789727576807.pdf'
F7 = 'Knuth2008_The Art Of Computer Programming_9780321534965.pdf'
F8 = 'Man2001_Genetic Algorithms Concepts And Designs_9781852330729.pdf'
F9 = "O'Connor2012_Violent Python A Cookbook for Hackers, Forensic Analysts, Penetra_9781597499644.pdf"
F10 = '海明威2007_Lao ren yu hai_9787500117018.pdf'

F11 = 'myfile.pdf'

FISBN = [F1, F2, F3, F4, F5]
FFT = [F6, F7, F8, F9, F10]
FILES = FISBN + FFT + [F11]


def create_files(files):
    os.chdir(os.path.dirname(TESTFILE))
    for fn in files:
        f = open(fn, 'w')
        f.write('ooo' + fn)
        f.close()


def delete_files(fnpatt):
    os.chdir(os.path.dirname(TESTFILE))
    for fn in cwdfiles(fnpatt):
        os.remove(fn)


def setup_module():
    create_files([TESTFILE, '/tmp/海明威-deleteme-PLEASE.pdf'])
    os.chdir(os.path.dirname(TESTFILE))
    create_files(FISBN+[F11])


def teardown_module():
    delete_files("*.pdf")


def test_ren():
    ren(F1)
    assert_equals('Knuth2008_The Art Of Computer Programming_9780321534965.pdf' in cwdfiles("*.pdf"), True)
    create_files([F5])
    ren(F5)
    assert_equals('Campos2011_Emergências obstétricas_9789727576807.pdf' in cwdfiles("*.pdf"), True)
    ren(F2)
    assert_equals("O'Connor2012_Violent Python A Cookbook For Hackers Forensic Analysts Penetration Testers_9781597499644.pdf" in cwdfiles("*.pdf"), True)
    ren(F4)
    assert_equals("海明威2007_Lao ren yu hai_9787500117018.pdf" in cwdfiles("*.pdf"), True)

