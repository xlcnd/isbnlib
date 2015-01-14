
For Devs
========


API's Main Namespaces
---------------------

In the namespace ``isbnlib`` you have access to the core methods:
``is_isbn10``, ``is_isbn13``, ``to_isbn10``, ``to_isbn13``, ``canonical``,
``clean``, ``notisbn``, ``get_isbnlike``, ``get_canonical_isbn``, ``mask``,
``meta``, ``info``, ``editions``, and ``isbn_from_words``.
The exceptions raised by these methods can all be catched using ``isbnlibException``.

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
  ``vias.multi`` to use several cores. The default is ``vias.serial``, but
  you can change that in the conf file.

* ``bouth23`` a small module to make it possible the code to run in
  **bouth** python 2 and python 3.


The exceptions raised by these methods can all be catched using ``ISBNLibDevException``.


In ``isbnlib.dev.helpers`` you can find several methods, that we found very useful,
but you should consider them as beta software. They can change a lot in
the future.



All these classes follow a simple design pattern and, if you follow it, will be
very easy to integrate your classes with the rest of the lib.




Merge Metadata
--------------

The original quality of metadata, at the several services, is not very good!
If you need high quality metadata in your app, the only solution is to use
*polling & merge* of several providers **and** a **lot** of cleaning and standardization
for fields like ``Authors`` and ``Publisher``.
A *simple merge* provider is now the default in ``isbnlib.meta``.
It gives priority to ``wcat`` but overwrites the ``Authors`` field with the value from ``goob``.
Uses the ``merge`` method of ``Metadata`` and *serial* calls to services
by default (faster for fast Internet connections).
You can write your own *merging scheme* by creating a new provider (see_ ``merge`` for an example).

    **Take Note**: These classes are optimized for one-calls to services and not for batch calls.


A full featured app!
--------------------

If you want a full featured app, that uses ``isbnlib``, with end users apps, configuration files and a 
framework to further developement, take a look at isbntools_.

---------------------------------------------------------------------------------

**You can browse the code, in a very structured way, at** sourcegraph_ or GitHub_.


.. _wcat: https://github.com/xlcnd/isbnlib/blob/master/isbnlib/_wcat.py

.. _isbndb: https://github.com/xlcnd/isbnlib/blob/master/isbnlib/_isbndb.py

.. _see: https://github.com/xlcnd/isbnlib/blob/master/isbnlib/_merge.py

.. _GitHub: https://github.com/xlcnd/isbnlib

.. _sourcegraph: https://sourcegraph.com/github.com/xlcnd/isbnlib

.. _isbntools: https://github.com/xlcnd/isbntools
