# -*- coding: utf-8 -*-
"""Interface for namespace 'isbnlib.dev'."""

from ._data import Metadata, stdmeta
from ._decorators import cache
from ._exceptions import (
    DataNotFoundAtServiceError,
    DataWrongShapeError,
    ISBNLibDevException,
    ISBNLibHTTPError,
    ISBNLibURLError,
    NoAPIKeyError,
    NoDataForSelectorError,
    NotValidMetadataError,
    RecordMappingError,
    ServiceIsDownError,
)
from .webquery import WEBQuery
from .webservice import WEBService

__all__ = (
    'ISBNLibDevException',
    'ISBNLibURLError',
    'ISBNLibHTTPError',
    'DataNotFoundAtServiceError',
    'ServiceIsDownError',
    'DataWrongShapeError',
    'NotValidMetadataError',
    'NoDataForSelectorError',
    'RecordMappingError',
    'NoAPIKeyError',
    'Metadata',
    'stdmeta',
    'WEBService',
    'WEBQuery',
    'cache',
)
