# -*- coding: utf-8 -*-
"""Interface for namespace 'isbnlib.dev'."""

from . import helpers, vias
from ._data import Metadata, stdmeta
from ._decorators import cache
from ._exceptions import (DataNotFoundAtServiceError, DataWrongShapeError,
                          ISBNLibDevException, ISBNLibHTTPError,
                          ISBNLibURLError, NoAPIKeyError,
                          NoDataForSelectorError, NotValidMetadataError,
                          RecordMappingError, ServiceIsDownError)
from .webquery import WEBQuery
from .webservice import WEBService

# alias
ISBNToolsDevException = ISBNLibDevException
ISBNToolsHTTPError = ISBNLibHTTPError
ISBNToolsURLError = ISBNLibURLError

__all__ = ('ISBNToolsDevException', 'ISBNLibDevException',
           'ISBNToolsHTTPError', 'ISBNToolsURLError', 'ISBNLibHTTPError',
           'ISBNLibURLError', 'DataNotFoundAtServiceError',
           'ServiceIsDownError', 'DataWrongShapeError',
           'NotValidMetadataError', 'NoDataForSelectorError',
           'RecordMappingError', 'NoAPIKeyError', 'Metadata', 'stdmeta',
           'WEBService', 'WEBQuery', 'vias', 'helpers', 'cache')
