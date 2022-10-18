# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file

from .._core import (
    EAN13,
    _check_structure10,
    _check_structure13,
    canonical,
    check_digit10,
    check_digit13,
    clean,
    ean13,
    get_canonical_isbn,
    get_isbnlike,
    is_isbn10,
    is_isbn13,
    notisbn,
    to_isbn10,
    to_isbn13,
)
from .data4tests import ISBNs

# tests


def test_check_digit10():
    """Test check digit algo for ISBN-10."""
    assert check_digit10('082649752') == '7'
    assert check_digit10('585270001') == '0'
    assert check_digit10('08264975X') == ''
    assert check_digit10('08264975') == ''


def test_check_digit13():
    """Test check digit algo for ISBN-13."""
    assert check_digit13('978082649752') == '9'
    assert check_digit13('97808264975') == ''
    assert check_digit13('97808264975X') == ''


def test__check_structure10():
    """Test structure detection for ISBN-10."""
    assert _check_structure10('0826497527') == True
    assert _check_structure10('0826497X27') == True  # isbnlike!
    assert _check_structure10('0826497XI7') == False


def test__check_structure13():
    """Test structure detection for ISBN-13."""
    assert _check_structure13('9780826497529') == True
    assert _check_structure13('978082649752X') == False


def test_is_isbn10():
    """Test detection and validation for ISBN-10."""
    assert is_isbn10('0826497527') == True
    assert is_isbn10('isbn 0-8264-9752-7') == True
    assert is_isbn10('0826497520') == False
    assert is_isbn10('954430603X') == True


def test_is_isbn13():
    """Test detection and validation for ISBN-13."""
    assert is_isbn13('9780826497529') == True
    assert is_isbn13('9791090636071') == True
    assert is_isbn13('isbn 979-10-90636-07-1') == True
    assert is_isbn13('9780826497520') == False
    assert is_isbn13('9700000000000') == False
    assert is_isbn13('9000000000000') == False
    assert is_isbn13('9710000000000') == False


def test_to_isbn10():
    """Test transformation of ISBN to ISBN-10."""
    assert to_isbn10('9780826497529') == '0826497527'
    assert to_isbn10('0826497527') == '0826497527'
    assert to_isbn10('9780826497520') == ''  # ISBN13 not valid
    assert to_isbn10('9790826497529') == ''
    assert to_isbn10('97808264975X3') == ''
    assert to_isbn10('978-826497') == ''  # (bug #14)
    assert to_isbn10('isbn 0-8264-9752-7') == '0826497527'
    assert to_isbn10('isbn 979-10-90636-07-1') == ''
    assert to_isbn10('isbn 978-0-8264-9752-9') == '0826497527'
    assert to_isbn10('asdadv isbn 978-0-8264-9752-9') == '0826497527'


def test_to_isbn13():
    """Test transformation of ISBN to ISBN-13."""
    assert to_isbn13('0826497527') == '9780826497529'
    assert to_isbn13('9780826497529') == '9780826497529'
    assert to_isbn13('0826497520') == ''  # ISBN10 not valid
    assert to_isbn13('08X6497527') == ''
    assert to_isbn13('91-43-01019-9') == '9789143010190'  # (bug #14)
    assert to_isbn13('isbn 91-43-01019-9') == '9789143010190'
    assert to_isbn13('asd isbn 979-10-90636-07-1 blabla') == '9791090636071'


def test_clean():
    """Test the cleaning of ISBN-like strings."""
    assert clean(' 978.0826.497529') == '9780826497529'
    assert clean('ISBN: 9791090636071') == 'ISBN 9791090636071'
    assert clean('978,0826497520') == '9780826497520'


def test_notisbn():
    """Test the impossibility of extracting valid ISBN from ISBN-like strings."""
    assert notisbn('0826497527') == False
    assert notisbn('0826497520') == True
    assert notisbn('9780826497529', level='strict') == False
    assert notisbn('9426497529', level='strict') == True
    assert notisbn('978082649752', level='strict') == True
    assert notisbn('978082649752', level='loose') == True
    assert notisbn('9780826400001', level='loose') == False
    assert notisbn('9780826400001', level='strict') == True
    assert notisbn('9780826400001', level='badlevel') == None
    assert notisbn('978 9426497529') == True
    assert notisbn('9789426497529') == True
    assert notisbn('979 10 9063607 1') == False
    assert notisbn('9780826497520') == True


def test_get_isbnlike():
    """Test the extraction of ISBN-like strings."""
    assert len(get_isbnlike(ISBNs)) == 79
    assert len(get_isbnlike(ISBNs, 'normal')) == 79
    assert len(get_isbnlike(ISBNs, 'strict')) == 69
    assert len(get_isbnlike(ISBNs, 'loose')) == 81
    assert get_isbnlike(ISBNs, 'e') == []
    # issue 60 and 103
    # TODO add test...
    # issue 107
    assert get_isbnlike('978-0-9790173-4-6', 'normal')[0] == '978-0-9790173-4-6'
    assert get_isbnlike('978-9788461784', 'normal')[0] == '978-9788461784'


def test_get_canonical_isbn():
    """Test the extraction of canonical ISBN from ISBN-like string."""
    assert get_canonical_isbn('0826497527', output='bouth') == '0826497527'
    assert get_canonical_isbn('0826497527') == '0826497527'
    assert get_canonical_isbn('0826497527', output='isbn10') == '0826497527'
    assert get_canonical_isbn('0826497527', output='isbn13') == '9780826497529'
    assert (
        get_canonical_isbn('ISBN 0826497527', output='isbn13') == '9780826497529')
    assert get_canonical_isbn('ISBN 0826497527', output='NOOPTION') == ''
    assert get_canonical_isbn('0826497520') == ''
    assert get_canonical_isbn('9780826497529') == '9780826497529'
    assert get_canonical_isbn('9780826497520') == ''
    assert get_canonical_isbn('OSX 9780826497529.pdf') == '9780826497529'


def test_canonical():
    """Test the extraction of 'only numbers and X' from ISBN-like string."""
    assert canonical('ISBN 9789720404427') == '9789720404427'
    assert canonical('ISBN-9780826497529') == '9780826497529'
    assert canonical('ISBN9780826497529') == '9780826497529'
    assert canonical('isbn9780826497529') == '9780826497529'
    assert canonical('isbn 0826497527') == '0826497527'
    assert canonical('954430603x') == '954430603X'
    assert canonical('95443060x3') == ''
    assert canonical('0000000000') == ''
    assert canonical('000000000X') == ''
    assert canonical('0000000000000') == ''
    assert canonical('0000000') == ''
    assert canonical('') == ''


def test_ean13():
    """Test the extraction and validation of EAN13 from ISBN-like string."""
    assert ean13('ISBN 9789720404427') == ''
    assert ean13('ISBN 9789720404428') == '9789720404428'
    assert EAN13('ISBN-9780826497529') == '9780826497529'
    assert ean13('ISBN9780826497529') == '9780826497529'
    assert EAN13('isbn9780826497529') == '9780826497529'
    assert EAN13('isbn 0826497527') == '9780826497529'
    assert ean13('9700000000000') == ''
    assert EAN13('9000000000000') == ''
    assert EAN13('9710000000000') == ''
