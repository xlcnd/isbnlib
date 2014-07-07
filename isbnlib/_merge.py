# -*- coding: utf-8 -*-
"""Provide metadata by merging metadata from other providers."""

from ._wcat import query as qwcat
from ._goob import query as qgoob
from .dev import vias, Metadata
from . import config


def query(isbn, processor=None):
    """Query function for the `merge provider` (waterfall model)."""
    if not processor:
        processor = config.options.get('VIAS_MERGE', processor).lower()
        if not processor:     # pragma: no cover
            processor = 'serial'

    named_tasks = (('wcat', qwcat), ('goob', qgoob))
    if processor == 'parallel':
        results = vias.parallel(named_tasks, isbn)
    elif processor == 'serial':
        results = vias.serial(named_tasks, isbn)
    elif processor == 'multi':
        results = vias.multi(named_tasks, isbn)

    rw = results.get('wcat')
    rg = results.get('goob')

    md = Metadata(rw) if rw else None

    if md and rg:
        md.merge(rg, ('Authors'))
        return md.value
    if not md and rg:       # pragma: no cover
        md = Metadata(rg)
        return md.value
    return md.value if not rg and rw else None  # pragma: no cover
