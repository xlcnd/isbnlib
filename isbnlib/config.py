# -*- coding: utf-8 -*-
"""Config file for isbnlib."""

# --> Import only external modules! <--


import socket

# Timeouts
SOCKETS_TIMEOUT = 12    # seconds
THREADS_TIMEOUT = 11    # seconds


def setsocketstimeout(seconds):
    """Set the value of SOCKETS_TIMEOUT (in seconds)."""
    global SOCKETS_TIMEOUT
    SOCKETS_TIMEOUT = seconds
    return socket.setdefaulttimeout(SOCKETS_TIMEOUT)

# socket timeout is not exposed at urllib2 level so I had to import the
# module and set a default value for all the sockets (timeout in seconds)
# however this should be done at top level due to strong side effects...
setsocketstimeout(SOCKETS_TIMEOUT)


# THREADS_TIMEOUT is a parameter used downstream by Thread calls (see vias.py)
def setthreadstimeout(seconds):   # pragma: no cover
    """Set the value of THREADS_TIMEOUT (in seconds)."""
    global THREADS_TIMEOUT
    THREADS_TIMEOUT = seconds


# API keys
apikeys = {}


def add_apikey(service, apikey):  # pragma: no cover
    """Add API keys.

    add_apikey('isbndb', 'JuHytr6') [is fake!]
    """
    apikeys[service] = apikey


# Generic Options
options = {'VIAS_MERGE': 'serial'}


def set_option(option, value):    # pragma: no cover
    """Set the value for option."""
    options[option] = value
