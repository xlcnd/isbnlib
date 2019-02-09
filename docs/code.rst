====
Code
====



Search
------

Search/Browse the code at sourcegraph_ or github_



Status
------


.. image:: https://img.shields.io/badge/Sourcegraph-Status-blue.svg
    :target: https://sourcegraph.com/github.com/xlcnd/isbnlib
    :alt: Graph

.. image:: https://coveralls.io/repos/github/xlcnd/isbnlib/badge.svg?branch=v3.9.5
    :target: https://coveralls.io/github/xlcnd/isbnlib?branch=v3.9.5
    :alt: Coverage Status

.. image:: https://travis-ci.org/xlcnd/isbnlib.svg?branch=v3.9.5
    :target: https://travis-ci.org/xlcnd/isbnlib
    :alt: Built Status

.. image:: https://ci.appveyor.com/api/projects/status/github/xlcnd/isbnlib?branch=v3.9.5&svg=true
    :target: https://ci.appveyor.com/project/xlcnd/isbnlib
    :alt: Windows Built Status

.. image:: https://img.shields.io/pypi/dm/isbnlib.svg?style=flat
    :target: https://pypi.org/project/isbnlib/
    :alt: PYPI Downloads


-------------------------------------------------------------------------------------------------------


How to Contribute
-----------------

``isbnlib`` has a very small code base, so it is a good project to begin your
adventure in open-source...


Main Steps
^^^^^^^^^^

1. Make sure you have a GitHub account_
2. Submit a ticket for your issue or idea,
   on GitHub issues_
   (if possible wait for some feedback before any serious commitment... :)
3. Fork the repository on GitHub
4. ``pip install -r requirements-dev.txt``
5. Do your code... (**remember the code must run on python 2.6, 2.7, 3.3, 3.4, pypy
   and be OS independent**) (you will find ``travis-ci.org`` very handy for this!)
6. Write tests for your code using ``nose`` and put then in the directory ``isbnlib/test``
7. Pass **all tests** and with **coverage > 90%**.
   Check the coverage in Coveralls_.
8. **Check if all requirements are fulfilled**!
9. Make a pull request on github...



Important
^^^^^^^^^

If you don't have experience in these issues, don't be put off by these requirements,
see them as a learning opportunity. Thanks!

    For full instructions read the CONTRIBUTING_ doc.


.. _sourcegraph: https://sourcegraph.com/github.com/xlcnd/isbnlib
.. _github: https://github.com/xlcnd/isbnlib
.. _account: https://github.com/signup/free
.. _issues: https://github.com/xlcnd/isbnlib/issues
.. _Coveralls: https://coveralls.io/r/xlcnd/isbnlib
.. _CONTRIBUTING: https://github.com/xlcnd/isbnlib/blob/master/CONTRIBUTING.md

