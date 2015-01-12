

Known Issues
============

1. The ``meta`` method and the ``isbn_meta`` script sometimes give a wrong result
   (this is due to errors on the chosen service), in alternative you could
   try one of the others services.

2. The ``isbntools`` works internally with unicode, however this doesn't
   solve errors of lost information due to bad encode/decode at the origin!

3. Periodically, agencies, issue new blocks of ISBNs. The
   range_ of these blocks is on a database that ``mask`` uses. So it could happen,
   if you have a version of ``isbntools`` that is too old, ``mask`` doesn't work for
   valid (recent) issued ISBNs. The solution? **Update isbntools often**!

4. Calls to metadata services are cached by default. If you don't want this
   feature, just enter ``isbn_conf setopt cache no``. If by any reason you need
   to clear the cache, just enter ``isbn_conf delcache``.


Any issue that you would like to report, please do it at github_ (if you are a
dev) or at twitter_ (if you are an end user).




.. _github: https://github.com/xlcnd/isbntools/issues?labels=info&page=1&state=open

.. _range: https://www.isbn-international.org/range_file_generation

.. _here: http://isbndb.com/api/v2/docs

.. _wcat: https://github.com/xlcnd/isbntools/blob/master/isbntools/dev/wcat.py

.. _isbndb: https://github.com/xlcnd/isbntools/blob/master/isbntools/dev/isbndb.py

.. _see: https://github.com/xlcnd/isbntools/blob/master/isbntools/dev/merge.py

.. _help: https://github.com/xlcnd/isbntools/issues/8

.. _standalone: http://bit.ly/1i8qatY

.. _twitter: https://twitter.com/isbntools
