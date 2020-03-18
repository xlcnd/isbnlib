
.. image:: https://img.shields.io/badge/source-analyze-blue.svg?style=flat
    :target: https://sourcegraph.com/github.com/xlcnd/isbnlib
    :alt: Graph

.. image:: https://readthedocs.org/projects/isbnlib/badge/?version=latest
    :target: https://isbnlib.readthedocs.org/en/latest/
    :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/xlcnd/isbnlib/badge.svg?branch=master
    :target: https://coveralls.io/github/xlcnd/isbnlib?branch=master
    :alt: Coverage Status

.. image:: https://img.shields.io/travis/xlcnd/isbnlib/v3.10.0?label=travis&svg=true&style=flat
    :target: https://travis-ci.org/xlcnd/isbnlib
    :alt: Built Status

.. image:: https://ci.appveyor.com/api/projects/status/github/xlcnd/isbnlib?branch=v3.10.0&svg=true
    :target: https://ci.appveyor.com/project/xlcnd/isbnlib
    :alt: Windows Built Status

.. image:: https://img.shields.io/github/issues/xlcnd/isbnlib/bug.svg?label=bugs&style=flat
    :target: https://github.com/xlcnd/isbnlib/labels/bug
    :alt: Bugs

.. image:: https://img.shields.io/pypi/dm/isbnlib.svg?style=flat
    :target: https://pypi.org/project/isbnlib/
    :alt: PYPI Downloads


Warning
=======

   The releases 3.10.* will be the last to support python 2.7!


Info
====

``isbnlib`` is a (pure) python library that provides several
useful methods and functions to validate, clean, transform, hyphenate and
get metadata for ISBN strings. Its origin was as the core of isbntools_.

This short version, is suitable to be include as a dependency in other projects.
Has a straightforward setup and a very easy programmatic api.

Runs on py27, py35, py36, py37 and py38.

Typical usage (as library):

.. code-block:: python

    import isbnlib
    ...



ISBN
----

   The official form of an ISBN is something like ``ISBN 979-10-90636-07-1``. However for most
   applications only the numbers are important, you can always 'mask' them if you need (see below).
   This library works mainly with 'striped' ISBNs  (only digits and X) like '0826497527'. You can
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

   If possible, work with ISBNs in the isbn-13 format (since 2007, only are issued ISBNs
   in the isbn-13 format). You can always convert isbn-10 to isbn-13, but **not** the reverse.
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
    Keeps only digits and X. You will get strings like `9780321534965` and `954430603X`.

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

``meta(isbn, service='default')``
    Gives you the main metadata associated with the ISBN. As `service` parameter you can use:
    ``'goob'`` uses the **Google Books service** (**no key is needed**)  and
    **is the default option**,
    ``'openl'`` uses the **OpenLibrary.org** api (**no key is needed**).
    You can enter API keys
    with ``config.add_apikey(service, apikey)`` (see example below).
    The output can be formatted as ``bibtex``, ``csl`` (CSL-JSON), ``msword``, ``endnote``, ``refworks``,
    ``opf`` or ``json`` (BibJSON) bibliographic formats with ``registry.bibformatters``.
    Now, you can extend the functionality of this function by adding pluggins, more metadata
    providers or new bibliographic formatters (check_ for available pluggins).

``editions(isbn, service='merge')``
    Returns the list of ISBNs of editions related with this ISBN. By default
    uses 'merge' (merges 'openl' and 'thingl'), but other providers are available:
    'openl' users **Open Library**, 'thingl' (uses the service ThingISBN from **LibraryThing**)
    and 'any' (first tries 'openl', if no data, then 'thingl').

``isbn_from_words(words)``
    Returns the most probable ISBN from a list of words (for your geographic area).

``goom(words)``
    Returns a list of references from **Google Books multiple references**.

``classify(isbn)`` **NEW**
    Returns a dictionary of **classifiers** for a canonical ISBN. For the meaning of these classifiers see OCLC_.
    Most of the data in the underlying service are for books in english.

``doi(isbn)``
    Returns a DOI's ISBN-A from a ISBN-13.

``doi2tex(DOI)``
    Returns metadata formated as BibTeX for a given DOI.

``ren(filename)``
    Renames a file using metadata from an ISBN in his filename.

``desc(isbn)``
    Returns a small description of the book.
    *Almost all data available are for US books!*

``cover(isbn)``
    Returns a dictionary with the url for cover.
    *Almost all data available are for US books!*


See files test_core_ and test_ext_ for **a lot of examples**.


Install
=======


From the command line, enter (in some cases you have to preced the
command with ``sudo``):


.. code-block:: bash

    $ pip install isbnlib


If you use linux systems, you can install using your distribution package
manager (all major distributions have packages ``python-isbnlib``
and ``python3-isbnlib``), however (usually) are **very old and don't work well anymore**!



For Devs
========


API's Main Namespaces
---------------------

In the namespace ``isbnlib`` you have access to the **core functions**:
``is_isbn10``, ``is_isbn13``, ``to_isbn10``, ``to_isbn13``, ``canonical``,
``clean``, ``notisbn``, ``get_isbnlike``, ``get_canonical_isbn``, ``mask``,
``info``, ``check_digit10``, ``check_digit13``, ``doi`` and ``EAN13``.

In addition, you have access to **metadata functions**, namely:
``meta``, ``editions``, ``ren``, ``desc``, ``cover``,
``goom``, ``classify``, ``doi2tex`` and ``isbn_from_words``.

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

The exceptions raised by these methods can all be catched using ``ISBNLibDevException``.
You **should't raise** this exception in your code, only raise the specific exceptions
exposed in ``isbnlib.dev`` whose name ends in Error.


In ``isbnlib.dev.helpers`` you can find several methods, that we found very useful, some of then
are only used in ``isbntools`` (*an app and framework* that uses ``isbnlib``).


With ``isbnlib.config`` you can read and set configuration options:
change timeouts with ``seturlopentimeout`` and ``setthreadstimeout``,
access api keys with ``apikeys`` and add new one with ``add_apikey``,
access and set generic and user-defined options with ``options.get('OPTION1')`` and ``set_option``.


Finally, from ``isbnlib.registry`` you can change the metadata service to be used by default
(``setdefaultservice``),
add a new service (``add_service``), access bibliographic formatters for metadata (``bibformatters``),
set the default formatter (``setdefaultbibformatter``), add new formatters (``add_bibformatter``) and
set a new cache (``set_cache``) (e.g. to switch off the chache ``set_cache(None)``).
The cache only works for calls through metadata functions. These changes only work for the 'current session',
so should be done always before calling other methods.


Let us concretize these points with a small example.

Suppose you want a small script to get metadata using ``Open Library`` formated in BibTeX.

A minimal script would be:


.. code-block:: python

    from isbnlib import meta
    from isbnlib.registry import bibformatters

    SERVICE = 'openl'

    # now you can use the service
    isbn = '9780446310789'
    bibtex = bibformatters['bibtex']
    print(bibtex(meta(isbn, SERVICE)))



Plugins
-------

You can extend the functionality of the library by adding plugins (for now, just
new metadata providers or new bibliographic formatters).

For available plugins check_ here.

After install, your plugin will blend transparently in ``isbnlib`` (you will have more options in ``meta`` and ``bibformatters``).

If you want to develop a plugin, start with this template_ and follow the instructions there. For inspiration take a look
at goob_.


Remember that plugins **must** support python 2.7 and python 3.5+ (see python-future.org_).



Patterns of Usage
-----------------

The library implements a very simple API with sensible defaults, but there are cases
that need your attention (see case 3 below).



A. You only need **core functions**:


.. code-block:: python

    # import the core functions you need
    from isbnlib import canonical, is_isbn10, is_isbn13

    isbn = canonical("978-0446310789")
    if is_isbn13(isbn):
        ...
    ...


B. You need also **metadata functions**, with **default config**:


.. code-block:: python

    from isbnlib import canonical, meta, description

    isbn = canonical("978-0446310789")
    data = meta(isbn)
    ...

C. You need also **metadata functions**, with **special config**:

   *Lets suppose you need to add an api key for a metadata plugin
   and change the cache too*.


.. code-block:: python

    from myapp.utils import MyCache

    # import the functions you need, plus 'config' and 'registry'
    from isbnlib import canonical, config, meta, registry

    # you should use 'config' first
    config.add_apikey('isbndb', 'kjshdfkjahsdflkjh')

    # then 'registry'
    registry.set_cache(MyCache())

    # Only now you should use metadata functions
    # (there are no adaptions for core functions,
    #  so they can be used at any moment)
    isbn = canonical("978-0446310789")
    data = meta(isbn, service="isbndb")
    ...


D. You want to build a **plugin** or use **isbnlib.dev** in your code:

   You should study very carefully the **public** methods in ``dir(isbnlib.dev)``.



Caveats
-------


1. These classes are optimized for one-call to services and not for batch calls.

2. If you inspect the library, you will see that there are a lot of private modules
   (their name starts with '_'). These modules **should not** be accessed directly since,
   with high probability, your program will break with a further version of the library!



Projects using *isbnlib*
------------------------

**isbntools**      https://github.com/xlcnd/isbntools

**isbnsrv**        https://github.com/xlcnd/isbnsrv

**Open Library**   https://github.com/internetarchive/openlibrary

**NYPL Library Simplified**  https://github.com/NYPL-Simplified

**Manubot**   https://github.com/manubot

**Spreads**  https://github.com/DIYBookScanner/spreads



See the full list here_.



Help
----


If you need help, please take a look at github_ or post a question on
stackoverflow_ .



----------------------------------------------------------------------------------------------

.. class:: center

Read ``isbnlib`` code in a very sctructured way at sourcegraph_ or 'the docs' at readthedocs_.

----------------------------------------------------------------------------------------------


.. _github: https://github.com/xlcnd/isbnlib/issues

.. _range: https://www.isbn-international.org/range_file_generation

.. _isbntools: https://pypi.python.org/pypi/isbntools

.. _sourcegraph: http://bit.ly/ISBNLib_srcgraph

.. _readthedocs: http://bit.ly/ISBNLib_rtd

.. _stackoverflow: http://stackoverflow.com/search?tab=newest&q=isbnlib

.. _test_core: https://github.com/xlcnd/isbnlib/blob/master/isbnlib/test/test_core.py

.. _test_ext: https://github.com/xlcnd/isbnlib/blob/master/isbnlib/test/test_ext.py

.. _isbn-international.org: https://www.isbn-international.org/content/what-isbn

.. _wikipedia: http://en.wikipedia.org/wiki/International_Standard_Book_Number

.. _python-future.org: http://python-future.org/compatible_idioms.html

.. _issue: https://github.com/xlcnd/isbnlib/issues/28

.. _check: https://pypi.python.org/pypi?%3Aaction=search&term=isbnlib_&submit=search

.. _template: https://github.com/xlcnd/isbnlib/blob/dev/PLUGIN.zip

.. _goob: https://github.com/xlcnd/isbnlib/blob/dev/isbnlib/_goob.py

.. _search: https://pypi.python.org/pypi?%3Aaction=search&term=isbnlib&submit=search

.. _51: https://github.com/xlcnd/isbnlib/issues/51

.. _here: https://github.com/xlcnd/isbnlib/network/dependents?package_id=UGFja2FnZS01MjIyODAxMQ%3D%3D

.. _OCLC: http://classify.oclc.org/classify2/


