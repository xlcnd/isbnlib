# -*- coding: utf-8 -*-
"""Config file for isbnlib."""

# --> Import only external modules! <--

# Timeouts
URLOPEN_TIMEOUT = 10  # seconds
THREADS_TIMEOUT = 12  # seconds


# URLOPEN_TIMEOUT is used by webservice
def seturlopentimeout(seconds):  # pragma: no cover
    """Set the value of URLOPEN_TIMEOUT (in seconds)."""
    global URLOPEN_TIMEOUT
    URLOPEN_TIMEOUT = seconds


# THREADS_TIMEOUT is a parameter used downstream by Thread calls (see vias.py)
def setthreadstimeout(seconds):  # pragma: no cover
    """Set the value of THREADS_TIMEOUT (in seconds)."""
    global THREADS_TIMEOUT
    THREADS_TIMEOUT = seconds


# API keys
apikeys = {}


def add_apikey(service, apikey):  # pragma: no cover
    """Add API keys."""
    global apikeys
    apikeys[service.lower()] = apikey


# Generic Options
options = {
    'LOAD_FORMATTER_PLUGINS': True,
    'LOAD_METADATA_PLUGINS': True,
    'VIAS_MERGE': 'parallel',
}


def set_option(option, value):  # pragma: no cover
    """Set the value for option."""
    global options
    options[option.upper()] = value


LOAD_METADATA_PLUGINS = options.get('LOAD_METADATA_PLUGINS', True)
LOAD_FORMATTER_PLUGINS = options.get('LOAD_FORMATTER_PLUGINS', True)


def setloadplugins(boolean=True):
    """Set the value for all LOAD_XXX_PLUGINS."""
    global options, LOAD_METADATA_PLUGINS, LOAD_FORMATTER_PLUGINS
    set_option('LOAD_METADATA_PLUGINS', boolean)
    set_option('LOAD_FORMATTER_PLUGINS', boolean)
    LOAD_METADATA_PLUGINS = boolean
    LOAD_FORMATTER_PLUGINS = boolean
