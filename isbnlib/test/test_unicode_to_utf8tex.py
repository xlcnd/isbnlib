# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file

from ..dev._helpers import unicode_to_utf8tex


def test_unicode_to_utf8tex():
    """Test 'unicode_to_utf8tex' identity transformation."""
    assert unicode_to_utf8tex(u'\u00E2 \u00F5') == b'\^{a}\space \~{o}'
    assert unicode_to_utf8tex(u'\u00E2 \u00F5', (b'\\space ',)) == b'\^{a} \~{o}'
