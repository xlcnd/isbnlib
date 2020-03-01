

Known Issues
============

1. The ``meta`` method sometimes give a wrong result
   (this is due to errors on the chosen service), in alternative you could
   try one of the others services.

2. The ``isbnlib`` works internally with unicode, however this doesn't
   solve errors of lost information due to bad encode/decode at the origin!

3. Periodically, agencies, issue new blocks of ISBNs. The
   range_ of these blocks is on a database that ``mask`` uses. So it could happen,
   if you have a version of ``isbnlib`` that is too old, ``mask`` doesn't work for
   valid (recent) issued ISBNs. The solution? **Update isbnlib often**!

4. Calls to metadata services are cached by default. You can change that by setting
   the cache to ``None``, namely ``registry.set_cache(None)``.


Any issue that you would like to report, please do it at github_ or post a question on
stackoverflow_ (with tag **isbnlib**).



.. _github: https://github.com/xlcnd/isbnlib/issues

.. _range: https://www.isbn-international.org/range_file_generation

.. _stackoverflow: http://stackoverflow.com/search?tab=newest&q=isbnlib
