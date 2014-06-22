# -*- coding: utf-8 -*-

"""Private helper functions."""

import re
import sys


def in_virtual():       # pragma: no cover
    """Detect if the program is running inside a python virtual environment."""
    return True if hasattr(sys, 'real_prefix') else False


def normalize_space(item):
    """Normalize white space.

    Strips leading and trailing white space and replaces sequences of
    white space characters with a single space.
    """
    item = re.sub(r'\s\s+', ' ', item)
    return item.strip()


def titlecase(s):
    """Format string in title case.

    Only changes the first character of each word.
    """
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda m: m.group(0)[0].upper() + m.group(0)[1:], s)


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
    """Replace unicode entities with tex entitites and returns utf8 bytes."""
    from .bouth23 import b, s
    from .._data.data4tex import unicode_to_tex
    btex = utex.encode('utf-8')
    table = dict((k.encode('utf-8'), v) for k, v in unicode_to_tex.items()
                 if v not in filtre)
    regex = re.compile(b('|'.join(re.escape(s(k)) for k in table)))
    return regex.sub(lambda m: table[m.group(0)], btex)


def cutoff_tokens(tokens, cutoff):
    """Keep only the tokens with total length <= cutoff."""
    ltokens = [len(t) for t in tokens]
    length = 0
    stokens = []
    for token, l in zip(tokens, ltokens):
        if length + l <= cutoff:
            length = length + l
            stokens.append(token)
        else:
            break
    return stokens


def parse_placeholders(pattern):
    """Return a list of placeholders in a pattern."""
    regex = re.compile(r'({[^}]*})')
    return regex.findall(pattern)
