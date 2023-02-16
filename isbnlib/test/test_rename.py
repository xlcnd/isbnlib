# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""
tests
"""

import locale
import os

import pytest

from .._ext import ren
from ..dev.helpers import cwdfiles

pytestmark = pytest.mark.network

WINDOWS = os.name == 'nt'
ENCODING = locale.getpreferredencoding()
if ENCODING != 'UTF-8':
    print(
        "Your default locale encoding (%s) doesn't allow unicode filenames!" % ENCODING,
    )
    print('=> Some tests could fail.')

TESTFILE_1 = './ç-deleteme.pdf' if WINDOWS else '/tmp/ç-deleteme.pdf'
TESTFILE_2 = './ç-deleteme-PLEASE.pdf' if WINDOWS else '/tmp/ç-deleteme-PLEASE.pdf'

# F1 = '9780321534965.pdf'
# F1 = '9780872203495.pdf'
F1 = '9780198520115.pdf'
F2 = '9781597499644.pdf'
F3 = '9781852330729.pdf'
F4 = '9787500117018.pdf'
F5 = '9789727576807.pdf'

# issue #60 (related with issue #107)
F6 = 'Campos2011_Emergências obstétricas_978-9727576807.pdf'
# F7 = 'Knuth2008_The Art Of Computer Programming_9780321534965.pdf'
# F7a = 'Knuth2008_Introduction To Combinatorial Algorithms And Boolean Functions_9780321534965.pdf'
# F7 = 'Plato1997_Complete Works_9780872203495.pdf'  # same as F1
F7 = 'Dirac1981_The Principles Of Quantum Mechanics_9780198520115.pdf'  # same as F1
F8 = 'Man2001_Genetic Algorithms Concepts And Designs_9781852330729.pdf'
F9 = "O'Connor2012_Violent Python A Cookbook for Hackers, Forensic Analysts, Penetra_9781597499644.pdf"
F10 = '海明威2007_Lao ren yu hai_9787500117018.pdf'

F11 = 'myfile.pdf'

FISBN = [F1, F2, F3, F4, F5]
FFT = [F6, F7, F8, F9, F10]
FILES = FISBN + FFT + [F11]


def create_files(files):
    os.chdir(os.path.dirname(TESTFILE_1))
    for fn in files:
        try:
            with open(fn, 'w') as f:
                f.write('ooo'.encode('utf-8') + fn.encode('utf-8'))
        except UnicodeEncodeError:
            print(
                "Your default locale (%s) doesn't allow non-ascii filenames!"
                % locale.CODESET,
            )


def delete_files(fnpatt):
    os.chdir(os.path.dirname(TESTFILE_1))
    for fn in cwdfiles(fnpatt):
        os.remove(fn)


def setup_module():
    # create_files([u(TESTFILE_1), u(TESTFILE_2)])
    os.chdir(os.path.dirname(TESTFILE_1))
    # create_files(FISBN + [F11])
    create_files([F1])


def teardown_module():
    delete_files('*.pdf')


def test_ren():
    """Test 'high level' ren function."""
    ren(F1)
    assert (F7 in cwdfiles('*.pdf')) == True
    # assert F7 in cwdfiles("*.pdf") or F7a in cwdfiles("*.pdf") is True
    # create_files([F5])
    # ren(F5)
    # assert 'Campos2011_Emergências obstétricas_9789727576807.pdf' in cwdfiles("*.pdf") is True
