Info
====

``isbnlib`` is a (pure) python library, based on isbntools_, that provides several
useful methods and functions to validate, clean, transform, hyphenate and
get metadata for ISBN strings.

This short version, is suitable to be include as a dependency in other projects.
Has a straightforward setup and a very easy programmatic api.


Typical usage (as library):

.. code-block:: python

    #!/usr/bin/env python
    import isbnlib
    ...


Main Functions
--------------

``is_isbn10(isbn10like)``
	Validate as ISBN-10.

``is_isbn13(isbn13like)``
	Validate as ISBN-13.

``to_isbn10(isbn13)``
	Transform isbn-13 to isbn-10.

``to_isbn13(isbn10)``
	Transform isbn-10 to isbn-13.

``canonical(isbnlike)``
	Keep only numbers and X. You will get strings like `9780321534965`.

``clean(isbnlike)``
	Clean ISBN (only legal characters).

``notisbn(isbnlike, level='strict')``
	Check with the goal to invalidate isbn-like.

``get_isbnlike(text, level='normal')``
	Extract all substrings that seem like ISBNs (very useful for scraping).

``get_canonical_isbn(isbnlike, output='bouth')``
	Extract ISBNs and transform them to the canonical form.

``EAN13(isbnlike)``
	Transform an `isbnlike` string into an EAN13 number (validated canonical ISBN-13).

``info(isbn)``
	Get language or country assigned to this ISBN.

``mask(isbn, separator='-')``
	`Mask` (hyphenate) a canonical ISBN.

``meta(isbn, service='default')``
    Gives you the main metadata associated with the ISBN. As `service` parameter you can use:
    ``'wcat'`` uses **worldcat.org**
    (**no key is needed**), ``'goob'`` uses the **Google Books service** (**no key is needed**),
    ``'isbndb'`` uses the **isbndb.com** service (**an api key is needed**),
    ``'openl'`` uses the **OpenLibrary.org** api (**no key is needed**), ``merge`` uses
    a merged record of ``wcat`` and ``goob`` records (**no key is needed**) and
    **is the default option**.
    You can get an API key for the *isbndb.com service* here_.  You can enter API keys
    with ``config.add_apikey(service, apikey)``.
    The output can be formatted as ``bibtex``, ``msword``, ``endnote``, ``refworks``,
    ``opf`` or ``json`` (BibJSON) bibliographic formats with ``dev.helpers.fmtbib``.

``editions(isbn)``
	Return the list of ISBNs of editions related with this ISBN.

``isbn_from_words(words)``
	Return the most probable ISBN from a list of words (for your geographic area).

``goom(words)``
	Return a list of references from **Google Books multiple references**.

``doi(isbn)``
	Return a DOI's ISBN-A from a ISBN-13.

``ren(filename)``
	Rename a file using metadata from an ISBN in his filename.



Install
=======

From the command line enter (in some cases you have to preced the
command with ``sudo``):


.. code-block:: bash

    $ pip install isbnlib

or:

.. code-block:: bash

    $ easy_install isbnlib



For Devs
========


Main Namespaces
---------------

In the namespace ``isbnlib`` you have access to the core methods:
``is_isbn10``, ``is_isbn13``, ``to_isbn10``, ``to_isbn13``, ``canonical``,
``clean``, ``notisbn``, ``get_isbnlike``, ``get_canonical_isbn``, ``mask``,
``meta``, ``info``, ``editions``, ``ren``, ``doi``, ``EAN13``
and ``isbn_from_words``.


You can extend the lib by using the classes and functions exposed in
namespace ``isbnlib.dev``, namely:

* ``WEBService`` a class that handles the access to web
  services (just by passing an url) and supports ``gzip``.
  You can subclass it to extend the functionality... but
  probably you don't need to use it! It is used in the next class.

* ``WEBQuery`` a class that uses ``WEBService`` to retrieve and parse
  data from a web service. You can build a new provider of metadata
  by subclassing this class.
  His main methods allow passing custom
  functions (*handlers*) that specialize them to specific needs (``data_checker`` and
  ``parser``).

* ``Metadata`` a class that structures, cleans and 'validates' records of
  metadata. His method ``merge`` allows to implement a simple merging
  procedure for records from different sources. The main features can be
  implemented by a call to ``stdmeta`` function!

* ``vias`` exposes several functions to put calls to services, just by passing the name and
  a pointer to the service's ``query`` function.
  ``vias.parallel`` allows to put threaded calls, however doesn't implement
  throttling! You can use ``vias.serial`` to make serial calls and
  ``vias.multi`` to use several cores. The default is ``vias.serial``.

* ``bouth23`` a small module to make it possible the code to run
  in **bouth** python 2 and python 3.


Merge Metadata
--------------

The original quality of metadata, at the several services, is not very good!
If you need high quality metadata in your app, the only solution is to use
*polling & merge* of several providers **and** a **lot** of cleaning and standardization
for fields like ``Authors`` and ``Publisher``.
A *merge* provider is now the default in ``meta``.
It gives priority to ``wcat`` but overwrites the ``Authors`` field with the value from ``goob``.
Uses the ``merge`` method of ``Metadata`` and *serial* calls to services
by default (faster for faster internet connections). You can change that by
using ``vias``'s other methods.


Helpers
-------

In ``isbnlib.dev.lab`` you can find several methods, that we found very useful, some of then
are only used in ``isbntools`` (*full version*).



Caveats
-------


1. These classes are optimized for one-calls to services and not for batch calls.

2. If you inspect the library, you will see that there are a lot of private modules
   (their name starts with '_'). These modules **should not** be accessed directly since,
   with high probability, your program will break with a further version of the library!

-------------------------------------------------------------

For the full library see isbntools_

-------------------------------------------------------------

.. _github: https://github.com/xlcnd/isbn/issues?labels=info&page=1&state=open

.. _range: https://www.isbn-international.org/range_file_generation

.. _here: http://isbndb.com/api/v2/docs

.. _isbntools: https://pypi.python.org/pypi/isbntools
