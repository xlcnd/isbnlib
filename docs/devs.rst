
For Devs
========


API's Main Namespaces
---------------------

In the namespace ``isbntools`` you have access to the core methods:
``is_isbn10``, ``is_isbn13``, ``to_isbn10``, ``to_isbn13``, ``canonical``,
``clean``, ``notisbn``, ``get_isbnlike``, ``get_canonical_isbn``, ``mask``,
``meta``, ``info``, ``editions``, and ``isbn_from_words``.
The exceptions raised by these methods can all be catched using ``ISBNToolsException``.

You can extend the lib by using the classes and functions exposed in
namespace ``isbntools.dev``, namely:

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
  ``vias.multi`` to use several cores. The default is ``vias.serial``, but
  you can change that in the conf file.

* ``bouth23`` a small module to make it possible the code to run in
  **bouth** python 2 and python 3.


The exceptions raised by these methods can all be catched using ``ISBNToolsDevException``.


In ``isbntools.dev.lab`` you can find several methods, that we found very useful,
but you should consider them as beta software. They can change a lot in
the future.


Finally, ``isbntools.conf`` provides methods to edit the configuration file and
helpers to work with isbntools's modules.


    **WARNING**: If you inspect the library, you will see that there are a lot of
    private modules (their name starts with '_'). These modules **should not**
    be accessed directly since, with high probability, your program will break
    with a further version of the library!

    You should access only methods in the API's ``isbntools``, ``isbntools.dev``,
    ``isbntools.dev.lab`` and ``isbntools.conf``



All these classes follow a simple design pattern and, if you follow it, will be
very easy to integrate your classes with the rest of the lib.


Plugins
-------

One easy way to do that, is to write a new metadata provider that will work as a **plugin**.
(You can use as source a web service, a database, ... ). We just had to follow these steps:

1. Write a python file with a short name, let us say ``goodr.py``. You can
   follow as models wcat_ or isbndb_, but the only **mandatory** requirement is
   that it **must** have a function called ``query``, with signature
   ``query(isbn)``, and that **must** return records in a standard form (like ``wcat`` for
   example). One way to garantee that, is by *returning* with ``return
   stdmeta(records)``. You can **download a template for a plugin** here_.

2. Create a new section called ``[PLUGINS]`` in ``isbntools.conf`` and, for the
   example above, enter a new line like this ``goodr=/full/path/to/directory/of/py/file``.
   **In alternative**, you can use *setuptools's entry points* and enter in your
   ``setup.py`` file something like this::

       entry_points = {
            'isbntools.plugin': ['goodr=mypackage.goodr:query'],
                       },
       install_requires=["isbntools>=3.3.6"],

3. If your plugin uses a service with an API key (e.g. qWeRTY), you must enter a new line in
   the ``[SERVICES]`` section like this ``GOODR_API_KEY=qWeRTY``.

Now you could use ``isbn_meta 9780321534965 goodr`` to get the metadata of ``9780321534965``.

If you think that your *service* could be useful to other persons, publish it to *pypi* using the
name ``isbntools.contrib.yourservice`` or clone the ``isbntools`` repository on GitHub_ and
make a pull request [help_]!


Merge Metadata
--------------

The original quality of metadata, at the several services, is not very good!
If you need high quality metadata in your app, the only solution is to use
*polling & merge* of several providers **and** a **lot** of cleaning and standardization
for fields like ``Authors`` and ``Publisher``.
A *simple merge* provider is now the default in ``isbn_meta`` (and ``isbntools.meta``).
It gives priority to ``wcat`` but overwrites the ``Authors`` field with the value from ``goob``.
Uses the ``merge`` method of ``Metadata`` and *serial* calls to services
by default (faster for fast Internet connections).
You can change that, by setting ``VIAS_MERGE=parallel`` or ``VIAS_MERGE=multi`` (see note below).
You can write your own *merging scheme* by creating a new provider (see_ ``merge`` for an example).

    **Take Note**: These classes are optimized for one-calls to services and not for batch calls.


Just an ISBN lib!
-----------------

If you just want to integrate the lib in your project, you have several options,
depending on your needs...

1. If you need only basic manipulation of ISBNs (validation, transforming,
   extraction, hyphenation, ...) but not metadata or file renaming,
   then you don't need a conf file. Just use the methods in ``isbntools``.
   Probably you are better served with isbnlib_.

2. If you rely heavily in metadata (or file renaming) and don't want to
   implement caching yourself, then you **need** an ``isbntools.conf`` file in a
   directory were your program could write.  You can use ``isbntools.conf`` to
   programatically manipulate the conf file.

3. If you want to vendorize the lib you should take a careful look at
   ``setup.py``!

Anyway, you could use the ``isbn_...`` scripts in the bin directory as examples
on how to use the library and as debugger tools for your implementation.

  **Don't forget** to take a look at isbnlib_.

---------------------------------------------------------------------------------

**You can browse the code, in a very structured way, at** sourcegraph_ (but not
the most recent version, for that go to GitHub_).


.. _wcat: https://github.com/xlcnd/isbntools/blob/master/isbntools/_wcat.py

.. _isbndb: https://github.com/xlcnd/isbntools/blob/master/isbntools/_isbndb.py

.. _see: https://github.com/xlcnd/isbntools/blob/master/isbntools/_merge.py

.. _here: https://github.com/xlcnd/isbntools/raw/dev/PLUGIN.zip

.. _help: http://bit.ly/1jcxq8W

.. _GitHub: http://bit.ly/1oTm5ze

.. _sourcegraph: http://bit.ly/1k14kHi

.. _isbnlib: http://bit.ly/ISBNlib
