#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Read and write shelve cache.


NOTES:
1. cannot use context manager for shelve because py2
2. shelve has different incompatible formats in py2 and py3
"""

import shelve
import datetime
from time import time as timestamp


class ShelveCache(object):

    """Read and write shelve cache."""

    def __init__(self, filepath):
        """Initialize attributes."""
        self._sh = shelve
        self.filepath = filepath
        try:
            s = self._sh.open(self.filepath)
        except:
            s = self._sh.open(self.filepath, 'n')
        s.close()

    def __getitem__(self, key):
        """Read cache."""
        try:
            s = self._sh.open(self.filepath)
            return s[key]['value'] if s[key] else None
        except KeyError:
            return None
        except ValueError:
            self.new()
            return None
        finally:
            s.close()

    def __setitem__(self, key, value):
        """Write to cache."""
        try:
            s = self._sh.open(self.filepath)
            s[key] = {'value': value, 'timestamp': timestamp()}
            status = True
        except:
            status = False
        finally:
            s.close()
        return status

    def __delitem__(self, key):
        """Delete record with key."""
        try:
            s = self._sh.open(self.filepath)
            del s[key]
        except KeyError:
            return
        except ValueError:
            self.new()
            return
        finally:
            s.close()

    def __len__(self):
        """Return the number of keys in cache."""
        return len(self.keys()) if self.keys() else 0

    def keys(self):
        """Return list of keys in Cache."""
        try:
            s = self._sh.open(self.filepath)
            return list(s.keys())
        finally:
            s.close()

    def ts(self, key):
        """Return the timestamp of the record with key."""
        try:
            s = self._sh.open(self.filepath)
            ts = s[key]['timestamp'] if s[key] else None
            if not ts:
                return
            fmt = '%Y-%m-%d %H:%M:%S'
            return datetime.datetime.fromtimestamp(ts).strftime(fmt)
        except KeyError:
            return
        except ValueError:
            self.new()
            return
        finally:
            s.close()

    def new(self):
        """Make new cache."""
        s = self._sh.open(self.filepath, 'n')
        s.close()
