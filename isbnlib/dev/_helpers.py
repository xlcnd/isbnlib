# -*- coding: utf-8 -*-
"""Private helper functions."""

import re
from hashlib import md5


def fake_isbn(title, author='unkown', publisher='unkown', sid=1):
    """Produce a fake ISBN from the (title, author, publisher) of the book."""
    key = '%s %s %s' % (title, author, publisher)
    # normalize
    regex1 = re.compile(r'\?|,|\.|!|\:|;', re.I | re.M | re.S)
    regex2 = re.compile(r'\s\s+', re.I | re.M | re.S)
    key = regex1.sub(' ', key)
    key = regex2.sub(' ', key).strip().lower()
    # hash
    return (str(sid) + str(int(md5(key.encode('utf-8')).hexdigest()[:10], 16)))[:13]


def normalize_space(item):
    """Normalize white space.

    Strips leading and trailing white space and replaces sequences of
    white space characters with a single space.
    """
    item = re.sub(r'\s\s+', ' ', item)
    return item.strip()


def titlecase(st):
    """Format string in 'title case' (for ascii)."""
    try:
        st.encode('ascii')
        return re.sub(
            r"[A-Za-z]+('[A-Za-z]+)?",
            lambda m: m.group(0)[0].upper() + m.group(0)[1:],
            st,
        )
    except (UnicodeEncodeError, UnicodeDecodeError):  # pragma: no cover
        return st


def last_first(author):
    """Parse an author name into last (name) and first."""
    if ',' in author:
        tokens = author.split(',')
        last = tokens[0].strip()
        first = ' '.join(tokens[1:]).strip().replace('  ', ', ')
    else:
        tokens = author.split(' ')
        last = tokens[-1].strip()
        first = ' '.join(tokens[:-1]).strip()
    return {'last': last, 'first': first}


def unicode_to_utf8tex(utex, filtre=()):
    """Replace unicode entities with tex entities and returns utf8 bytes."""
    from .._data.data4tex import unicode_to_tex

    btex = utex.encode('utf-8')
    table = {
        k.encode('utf-8'): v
        for k, v in unicode_to_tex.items() if v not in filtre
    }
    regex = re.compile('|'.join(re.escape(k.decode('utf-8', 'ignore')) for k in table).encode('utf-8'))
    return regex.sub(lambda m: table[m.group(0)], btex)


def cutoff_tokens(tokens, cutoff):
    """Keep only the tokens with total length <= cutoff."""
    ltokens = [len(t) for t in tokens]
    length = 0
    stokens = []
    for token, ln in zip(tokens, ltokens):
        if length + ln <= cutoff:
            length = length + ln
            stokens.append(token)
        else:
            break
    return stokens


def parse_placeholders(pattern):
    """Return a list of placeholders in a pattern."""
    regex = re.compile(r'({[^}]*})')
    return regex.findall(pattern)
