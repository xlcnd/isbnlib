
.. image:: https://sourcegraph.com/api/repos/github.com/xlcnd/isbnlib/.badges/status.svg
    :target: https://sourcegraph.com/github.com/xlcnd/isbnlib
    :alt: Graph

.. image:: https://readthedocs.org/projects/isbnlib/badge/?version=latest
    :target: http://isbnlib.readthedocs.org/en/latest/
    :alt: Documentation Status

.. image:: https://coveralls.io/repos/xlcnd/isbnlib/badge.svg?branch=v3.5.6
    :target: https://coveralls.io/r/xlcnd/isbnlib?branch=v3.5.6
    :alt: Coverage

.. image:: https://travis-ci.org/xlcnd/isbnlib.svg?branch=v3.5.6
    :target: https://travis-ci.org/xlcnd/isbnlib
    :alt: Built Status

.. image:: https://ci.appveyor.com/api/projects/status/github/xlcnd/isbnlib?branch=v3.5.6&svg=true
    :target: https://ci.appveyor.com/project/xlcnd/isbnlib
    :alt: Windows Built Status


Info
====

``isbnlib`` is a (pure) python library that provides several
useful methods and functions to validate, clean, transform, hyphenate and
get metadata for ISBN strings. Its origin was as the core of isbntools_.

This short version, is suitable to be include as a dependency in other projects.
Has a straightforward setup and a very easy programmatic api.


Typical usage (as library):

.. code-block:: python

    #!/usr/bin/env python
    import isbnlib
    ...



Note
----

   The official form of an ISBN is something like ``ISBN 979-10-90636-07-1``. However for most
   applications only the numbers are important, you can always 'masked' them if you need (see below).
   This library works mainly with 'striped' ISBNs  (only numbers and X) like '0826497527'. You can
   strip an ISBN-like string by using ``canonical(isbnlike)``. You can
   'mask' the ISBN by using ``mask(isbn)``. So in the examples below, when you see 'isbn'
   in the argument, it is a 'striped' ISBN, when the argument is an 'isbnlike' it is a string
   like ``ISBN 979-10-90636-07-1`` or even something dirty like ``asdf 979-10-90636-07-1 bla bla``.

   Two important concepts: **valid ISBN** should be an ISBN that was built according with the rules,
   this is distinct from **issued ISBN** that is an ISBN that was already issued to a publisher
   (this is the usage of the libraries and most of the web services).
   However *isbn.org*, probably by legal reasons, merges the two!
   So, according to *isbn-international.org*, '9786610326266' is not valid (because the block 978-66...
   has not been issued yet, however if you use ``is_isbn13('9786610326266')`` you will get ``True``
   (because '9786610326266' follows the rules of an ISBN). But the situation is even murkier,
   try ``meta('9786610326266')`` and you will see that this ISBN was already used!

   If possible, work with ISBNs in the isbn-13 format (since 2007, only are issued ISBNs in the isbn-13
   format). You can always convert isbn-10 to isbn-13, but **not** the reverse.
   Read more about ISBN at isbn-international.org_ or wikipedia_.



Main Functions
--------------

``is_isbn10(isbn10like)``
	Validates as ISBN-10.

``is_isbn13(isbn13like)``
	Validates as ISBN-13.

``to_isbn10(isbn13)``
	Transforms isbn-13 to isbn-10.

``to_isbn13(isbn10)``
	Transforms isbn-10 to isbn-13.

``canonical(isbnlike)``
	Keeps only numbers and X. You will get strings like `9780321534965` and `954430603X`.

``clean(isbnlike)``
	Cleans ISBN (only legal characters).

``notisbn(isbnlike, level='strict')``
	Check with the goal to invalidate isbn-like.

``get_isbnlike(text, level='normal')``
	Extracts all substrings that seem like ISBNs (very useful for scraping).

``get_canonical_isbn(isbnlike, output='bouth')``
	Extracts ISBNs and transform them to the canonical form.

``EAN13(isbnlike)``
	Transforms an `isbnlike` string into an EAN13 number (validated canonical ISBN-13).

``info(isbn)``
	Gets the language or country assigned to this ISBN.

``mask(isbn, separator='-')``
	`Mask` (hyphenate) a canonical ISBN.

``meta(isbn, service='default', cache='default')``
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
    ``opf`` or ``json`` (BibJSON) bibliographic formats with ``isbnlib.registry.bibformatters``.
    ``cache`` only allows two values: 'default' or None. You can change the kind of cache by using
    ``isbnlib.registry.set_cache`` (see below).

``editions(isbn, service='wcat')``
    Returns the list of ISBNs of editions related with this ISBN. By default
    uses 'wcat', but other providers are available: 'thingl' (uses the
    service ThingISBN from **LibraryThing**), 'merge' (merges 'wcat' with 'thingl')
    and 'any' (first tries 'wcat', if no data, tries 'thingl').

``isbn_from_words(words)``
	Returns the most probable ISBN from a list of words (for your geographic area).

``goom(words)``
	Returns a list of references from **Google Books multiple references**.

``doi(isbn)``
	Returns a DOI's ISBN-A from a ISBN-13.

``doi2tex(DOI)``
	Returns metadata formated as BibTeX for a given DOI.

``ren(filename)``
	Renames a file using metadata from an ISBN in his filename.

``desc(isbn)``
    **BETA** Returns a small description of the book.
    *Almost all data available are for US books!*

``cover(isbn)``
    **BETA** Downloads an image of the cover of the book or, with
    `cover(isbn, mode='url')`, returns an url of the image.
    *Almost all data available are for US books!*


See files test_core_ and test_ext_ for **a lot of examples**.


Install
=======

From the command line, enter (in some cases you have to preced the
command with ``sudo``):


.. code-block:: bash

    $ pip install isbnlib

or:

.. code-block:: bash

    $ easy_install isbnlib



For Devs
========


API's Main Namespaces
---------------------

In the namespace ``isbnlib`` you have access to the core methods:
``is_isbn10``, ``is_isbn13``, ``to_isbn10``, ``to_isbn13``, ``canonical``,
``clean``, ``notisbn``, ``get_isbnlike``, ``get_canonical_isbn``, ``mask``,
``meta``, ``info``, ``editions``, ``goom``, ``ren``, ``doi``, ``EAN13``,
``isbn_from_words``, ``desc`` and ``cover``.

The exceptions raised by these methods can all be catched using ``ISBNLibException``.


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
  ``parser``). It implements a **throttling mechanism** with a default rate of
  one call per second per service.

* ``Metadata`` a class that structures, cleans and 'validates' records of
  metadata. His method ``merge`` allows to implement a simple merging
  procedure for records from different sources. The main features of this class, can be
  implemented by a call to the ``stdmeta`` function instead!

* ``vias`` exposes several functions to put calls to services, just by passing the name and
  a pointer to the service's ``query`` function.
  ``vias.parallel`` allows to put threaded calls. 
  You can use ``vias.serial`` to make serial calls and
  ``vias.multi`` to use several cores. The default is ``vias.serial``.

* ``bouth23`` (**DEPRECATED**) a small module to make it possible the code to run
  in **bouth** python 2 and python 3. **It will disappear in the next major version!**.
  See python-future.org_ for a built-in alternative to ``bouth23``. 

The exceptions raised by these methods can all be catched using ``ISBNLibDevException``.
You **should't raise** this exception in your code, only raise the specific exceptions
exposed in ``isbnlib.dev`` whose name end in Error.


In ``isbnlib.dev.helpers`` you can find several methods, that we found very useful, some of then
are only used in ``isbntools`` (*an app and framework* that uses ``isbnlib``).


With ``isbnlib.registry`` you can change the metadata service to be used by default (``setdefaultservice``),
add a new service (``add_service``), access bibliographic formatters for metadata (``bibformatters``),
set the default formatter (``setdefaultbibformatter``), add new formatters (``add_bibformatter``) and
set a new cache (``set_cache``) (e.g. to switch off the chache ``set_cache(None)``).
The cache only works for calls through ``isbnlib.meta``. These changes only work for the 'current session',
so should be done always before calling other methods.


Finally, from ``isbnlib.config`` you can read and set configuration options:
change timeouts with ``setsocketstimeout`` and ``setthreadstimeout``,
access api keys with ``apikeys`` and add new one with ``add_apikey`` and
access and set generic and user-defined options with ``options`` and ``set_option``.




Merge Metadata
--------------

The original quality of metadata, at the several services, is not very good!
If you need high quality metadata in your app, the only solution is to use
*polling & merge* of several providers **and** a **lot** of cleaning and standardization
for fields like ``Authors`` and ``Publisher``.

A *merge* provider is now the default in ``meta``.
It gives priority to ``wcat`` but overwrites the ``Authors`` field with the value from ``goob``.
Uses the ``merge`` method of ``Metadata`` and *serial* calls to services
by default (faster for one-call to services through fast internet connections).
You can change that by using ``vias``'s other methods
(e.g. ``isbnlib.config.set_option('VIAS_MERGE', 'multi')``.


Caveats
-------


1. These classes are optimized for one-call to services and not for batch calls. However,
   is very easy to produce an high volume processing system using these classes
   (use ``vias.multi``) and Redis.

2. If you inspect the library, you will see that there are a lot of private modules
   (their name starts with '_'). These modules **should not** be accessed directly since,
   with high probability, your program will break with a further version of the library!



Help
____


If you need help, please take a look at github_ or post a question on
stackoverflow_ (with tag **isbnlib**)


----------------------------------------------------------------------------------------------

.. class:: center

Read ``isbnlib`` code in a very sctructured way at sourcegraph_ or 'the docs' at readthedocs_.

----------------------------------------------------------------------------------------------


.. _github: https://github.com/xlcnd/isbnlib/issues

.. _range: https://www.isbn-international.org/range_file_generation

.. _here: http://isbndb.com/api/v2/docs

.. _isbntools: https://pypi.python.org/pypi/isbntools

.. _sourcegraph: http://bit.ly/ISBNLib_srcgraph

.. _readthedocs: http://bit.ly/ISBNLib_rtd

.. _stackoverflow: http://stackoverflow.com/questions/tagged/isbnlib

.. _test_core: https://github.com/xlcnd/isbnlib/blob/master/isbnlib/test/test_core.py

.. _test_ext: https://github.com/xlcnd/isbnlib/blob/master/isbnlib/test/test_ext.py

.. _isbn-international.org: https://www.isbn-international.org/content/what-isbn

.. _wikipedia: http://en.wikipedia.org/wiki/International_Standard_Book_Number

.. _python-future.org: http://python-future.org/compatible_idioms.html
