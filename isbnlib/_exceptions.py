# -*- coding: utf-8 -*-
"""Exceptions for isbnlib."""

import sys


# pylint: disable=unused-argument
def quiet_errors(exc_type, exc_value, traceback):
    """Define error format suitable for end user scripts.

    Usage: enter the following lines in your script
    from isbnlib import quiet_errors
    sys.excepthook = quiet_errors
    """
    sys.stderr.write('Error: %s\n' % exc_value)  # pragma: no cover


class ISBNLibException(Exception):
    """Base class for isbnlib exceptions.

    This exception should not be raised directly,
    only subclasses of this exception should be used!
    """

    def __str__(self):
        """Print message."""
        return getattr(self, 'message', '')  # pragma: no cover


# pylint: disable=super-init-not-called
class NotRecognizedServiceError(ISBNLibException):
    """Exception raised when the service is not in config.py."""

    def __init__(self, service):
        """Define message."""
        self.message = '(%s) is not a recognized service' % service


# pylint: disable=super-init-not-called
class NotValidDefaultServiceError(ISBNLibException):
    """Exception raised when the service is not valid for default."""

    def __init__(self, service):
        """Define message."""
        self.message = '(%s) is not a valid default service' % service


# pylint: disable=super-init-not-called
class NotValidDefaultFormatterError(ISBNLibException):
    """Exception raised when the formatter is not valid for default."""

    def __init__(self, formatter):
        """Define message."""
        self.message = '(%s) is not a valid default formatter' % formatter


# pylint: disable=super-init-not-called
class NotValidISBNError(ISBNLibException):
    """Exception raised when the ISBN is not valid."""

    def __init__(self, isbnlike):
        """Define message."""
        self.message = '(%s) is not a valid ISBN' % isbnlike


# pylint: disable=super-init-not-called
class PluginNotLoadedError(ISBNLibException):  # pragma: no cover
    """Exception raised when the plugin's loader doesn't load the plugin.

    TODO: Delete this in version 4?
    """

    def __init__(self, path):
        """Define message."""
        self.message = "plugin (%s) wasn't loaded" % path
