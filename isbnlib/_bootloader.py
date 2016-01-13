# -*- coding: utf-8 -*-
"""Bootloader for plugins."""

# <--- NOTE: THIS CODE RUNS ON IMPORT! --->

from pkg_resources import iter_entry_points

from . import registry

# get plugins from entry_points
try:  # pragma: no cover
    for entry in iter_entry_points(group='isbnlib.metadata'):
        registry.add_service(entry.name, entry.load())
except:  # pragma: no cover
    pass

# get formatters from entry_points
try:  # pragma: no cover
    for entry in iter_entry_points(group='isbnlib.formatters'):
        registry.add_bibformatter(entry.name, entry.load())
except:  # pragma: no cover
    pass
