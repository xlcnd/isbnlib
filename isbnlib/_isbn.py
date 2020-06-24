# -*- coding: utf-8 -*-
"""Isbn class."""

import logging as _logging

from ._core import canonical, to_isbn10, EAN13
from ._exceptions import NotValidISBNError
from ._ext import mask, info, doi

LOGGER = _logging.getLogger(__name__)


# pylint: disable=useless-object-inheritance
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-few-public-methods
# pylint: disable=broad-except
class Isbn(object):
    """Class for ISBN objects."""

    def __init__(self, isbnlike):
        try:
            self.ean13 = EAN13(isbnlike)
            if not self.ean13:
                raise NotValidISBNError(isbnlike)
        except Exception:
            LOGGER.debug('error: %s is not a valid ISBN', isbnlike)
            raise NotValidISBNError(isbnlike)
        self.canonical = canonical(isbnlike)
        self.isbn13 = mask(self.ean13) or self.ean13
        self.isbn10 = mask(to_isbn10(self.ean13)) or to_isbn10(self.ean13)
        self.doi = doi(self.ean13)
        self.info = info(self.ean13)
        self.issued = '-' in self.isbn13

    def __str__(self):
        return str(vars(self))

    def __repr__(self):
        return self.__str__()
