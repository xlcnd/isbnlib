# -*- coding: utf-8 -*-
"""Return metadata, of a given DOI, formated as BibTeX."""

import logging

from .dev import cache
from .dev.webservice import query

LOGGER = logging.getLogger(__name__)

URL = 'http://dx.doi.org/{DOI}'
UA = 'isbnlib (gzip)'


@cache
def doi2tex(doi):
    """Get the bibtex ref for doi."""
    data = query(
        URL.format(DOI=doi),
        user_agent=UA,
        appheaders={
            'Accept': 'application/x-bibtex; charset=utf-8',
        },
    )  # noqa  pragma: no cover
    if not data:  # pragma: no cover
        LOGGER.warning('no data return for doi: %s', doi)
    return data if data else None  # pragma: no cover
