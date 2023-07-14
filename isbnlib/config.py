# -*- coding: utf-8 -*-
"""Config file for isbnlib."""

# --> Import only external modules! <--

# API keys
apikeys = {}


def add_apikey(service, apikey):  # pragma: no cover
    """Add API keys."""
    global apikeys
    apikeys[service.lower()] = apikey


# Options
options = {
    'LOAD_FORMATTER_PLUGINS': True,
    'LOAD_METADATA_PLUGINS': True,
    'THREADS_TIMEOUT': 12,  # seconds
    'URLOPEN_TIMEOUT': 10,  # seconds
    'VIAS_MERGE': 'parallel',
}


def set_option(option, value):  # pragma: no cover
    """Set the value for option."""
    global options
    options[option.upper()] = value


# URLOPEN_TIMEOUT is used by webservice
def seturlopentimeout(seconds):  # pragma: no cover
    """Set the value of URLOPEN_TIMEOUT (in seconds)."""
    set_option('URLOPEN_TIMEOUT', seconds)


# THREADS_TIMEOUT is a parameter used downstream by Thread calls (see vias.py)
def setthreadstimeout(seconds):  # pragma: no cover
    """Set the value of THREADS_TIMEOUT (in seconds)."""
    set_option('THREADS_TIMEOUT', seconds)


def setloadplugins(boolean=True):  # pragma: no cover
    """Set the value for all LOAD_XXX_PLUGINS."""
    set_option('LOAD_METADATA_PLUGINS', boolean)
    set_option('LOAD_FORMATTER_PLUGINS', boolean)
