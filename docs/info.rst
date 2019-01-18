

Info
====

``isbnlib`` is a (pure) python library that provides several
useful methods and functions to validate, clean, transform, hyphenate and
get metadata for ISBN strings. Its origin was as the core of isbntools_.

This short version, is suitable to be include as a dependency in other projects.
Has a straightforward setup and a very easy programmatic api.

Runs on py27, py34, py35, py36 and py37.


Usage
-----

Typical usage (as library):

.. code-block:: python

    import isbnlib
    ...


Just for fun, suppose I want the *most spoken about* book with certain words in his title.
For a *quick-and-dirty solution*, enter the following code in a file
and save it as ``isbn_tmsa_book.py``.

.. code-block:: python

    #!/usr/bin/env python
    import sys
    from isbnlib import *

    query = sys.argv[1].replace(' ', '+')
    isbn = isbn_from_words(query)

    print("The ISBN of the most `spoken-about` book with this title is %s" % isbn)
    print("")
    print("... and the book is:")
    print("")
    print((meta(isbn)))

Then in a command line (in the same directory):

.. code-block:: bash

    $ python isbn_tmsa_book.py 'noise'

In my case I get::


    The ISBN of the most `spoken-about` book with this title is 9780143105985

    ... and the book is:

    {'Publisher': u'Penguin Books', 'Language': u'eng', 'Title': u'White noise',
    'Year': u'2009', 'ISBN-13': u'9780143105985', 'Authors': u'Don DeLillo ;
    introduction by Richard Powers.'}


Have fun!



Projects using *isbnlib*
------------------------

**isbntools**      https://github.com/xlcnd/isbntools

**Open Library**   https://github.com/internetarchive/openlibrary

**Spreads**        https://github.com/DIYBookScanner/spreads

**Papis**    https://github.com/papis/papis

**libBMC**    https://github.com/Phyks/libbmc/

**Alessandria**     https://gitlab.com/openlabmatera/alessandria

**Comic Collector**  https://github.com/wengole/comiccollector

**Abelujo**    http://www.abelujo.cc/

**BibLib**    https://pypi.python.org/pypi/biblib




.. _pdfminer: https://pypi.python.org/pypi/pdfminer

.. _isbntools: https://pypi.python.org/pypi/isbntools
