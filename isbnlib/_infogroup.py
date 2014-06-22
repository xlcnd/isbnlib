# -*- coding: utf-8 -*-
"""Get the Language/Country of an ISBN."""

import logging
from ._data.data4info import d, identifiers, dnew, newidentifiers
from ._exceptions import NotValidISBNError

LOGGER = logging.getLogger(__name__)


def infogroup(isbn):
    """Get the Language/Country of this ISBN."""
    # if isbn is not a valid ISBN this def can give a wrong result!
    # -> do a minimal test
    if len(isbn) not in (10, 13):
        LOGGER.critical('%s is not a valid ISBN', isbn)
        raise NotValidISBNError(isbn)
    dtxt = d
    idents = identifiers
    ixi, ixf = 0, 1
    if len(isbn) == 13:
        ixi, ixf = 3, 4
        if isbn[0:3] == '979':
            ixf = 5  # <-- 979 id start with a group of 2 elements
            dtxt = dnew
            idents = newidentifiers
    for ident in idents:
        iid = isbn[ixi:ixf]
        ixf += 1
        # stop if identifier is found else continue!
        if iid in ident:
            return dtxt[iid]
