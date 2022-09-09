# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""
tests
"""

from .. import _gwords as words


def test_words():
    """Test 'isbn_from_words' function."""
    assert len(words.goos('the old man and the sea')) == 13
    # assert len(words.goos('Pessoa Desassossego')) == 13
    # assert words.goos('-ISBN -isbn') in ('9781364200329', None) == True
