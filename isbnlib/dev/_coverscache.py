# -*- coding: utf-8 -*-

"""Read and write cover cache.


    NOTE
    1. shelve has different incompatible formats in py2 and py3
    2. if some methods detect that the cache is not consistent
       they delete the cache and create a new one.
    3. After purge the cache keeps the records with more hits
       and the newests.
    4. The design is for safety not for performance! Increasing
       MAXLEN can have an high detrimental impact on performance.

    Examples:
    cc = CoversCache('.covers')
    cc['9781408835029'] = (
        "http://books.google.com/books/content?id=uUcvgfTYTRnjh"\
        "&printsec=frontcover"\
        "&img=1&zoom=2&edge=curl&source=gbs_api",
        ".covers/slot01/9781408835029.jpg"
        )
    cc['9781408835029']
    cc.hits('9781408835029')
    cc.keys()
    cc.files()
    cc.sync()
    cc.make()
    cc.delete()
    del cc['9781408835029']

"""

import os
import shutil
import sys
from random import randint

from ._shelvecache import ShelveCache

WINDOWS = os.name == 'nt'
PY3 = sys.version > '3'


class CoversCache(object):

    """Covers cache."""

    CACHEFOLDER = '.covers'
    INDEXFN = '.index'
    WINSHADOWIDX = INDEXFN + '.dat'
    MAXLEN = 3000
    NSLOTS = 10

    def __init__(self, cachepath=CACHEFOLDER):
        """Initialize attributes."""
        self.cachepath = cachepath
        self._indexpath = os.path.join(cachepath, self.INDEXFN)
        if WINDOWS and PY3:
            if not os.path.isfile(os.path.join(cachepath, self.WINSHADOWIDX)):
                self.make()
        elif not os.path.isfile(self._indexpath):
            self.make()
        self._index = ShelveCache(self._indexpath)
        self._index.MAXLEN = self.MAXLEN
        if len(self._index) > self.MAXLEN:
            self.purge()

    def __getitem__(self, key):
        """Read cache."""
        try:
            url, pth = self._index[key]
            pth = os.path.join(self.cachepath, pth)
            return (url, pth)
        except:
            return None

    def __setitem__(self, key, value):
        """Write to cache."""
        url, pth = value
        try:
            if pth and os.path.isfile(pth) and url:
                tocache = os.path.join(self._get_slot(), os.path.basename(pth))
                target = os.path.join(self.cachepath, tocache)
                shutil.copyfile(pth, target)
                if os.path.isfile(target):
                    self._index[key] = (url, tocache)
                    return True
                return False
            else:
                raise
        except:
            return False

    def __delitem__(self, key):
        """Delete record with key."""
        try:
            del self._index[key]
            return True
        except:
            return False

    def __len__(self):
        """Return the number of keys in cache."""
        return len(self._index.keys()) if self._index.keys() else 0

    def keys(self):
        """Return the number of keys in cache."""
        return self._index.keys()

    def hits(self, key):
        """Return the number of hits for key."""
        return self._index.hits(key)

    def _create_slots(self):
        for slot in range(self.NSLOTS):
            name = "slot%02d" % slot
            pth = os.path.join(self.cachepath, name)
            if not os.path.exists(pth):
                os.mkdir(pth)

    def make(self):
        """Init the cache."""
        # 1. Delete if available
        if os.path.isdir(self.cachepath):
            self.delete()
        # 2. Make folder
        os.mkdir(self.cachepath)
        # 3. Create Index
        self._index = ShelveCache(self._indexpath)
        # 4. Create slots
        self._create_slots()

    def _get_slot(self):
        return "slot%02d" % randint(0, self.NSLOTS - 1)

    def files(self):
        pths = []
        for root, _, fls in os.walk(self.cachepath):
            for fn in fls:
                pths.append(os.path.join(root, fn))
        return pths

    def sync(self):
        """Sync index entries with disk files."""
        # clear index entries not on disk
        checked = [self._indexpath]
        for key in self._index.keys():
            url, pth = self._index[key]
            pth = os.path.join(self.cachepath, pth)
            if not os.path.isfile(pth):
                self._index[key] = (url, None)
            checked.append(pth)
        # delete files not on index
        diff = tuple(set(self.files()) - set(checked))
        for fp in diff:
            if self.INDEXFN not in fp:
                os.remove(fp)

    def purge(self):
        try:
            self._index.purge()
            self.sync()
            return True
        except:
            return False

    def delete(self):
        self._index = None
        return shutil.rmtree(self.cachepath)
