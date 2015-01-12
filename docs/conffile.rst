

Conf File
=========

You can enter API keys and set preferences in the file ``isbntools.conf`` in your
``$HOME\.isbntools`` directory (UNIX). For Windows, you should look at
``%APPDATA%/isbntools/isbntools.conf``
(**create these, directory and file, if don't exist**  [Now just enter ``isbn_conf make``]).
The file should look like:

.. code-block:: bash

    [SYS]
    SOCKETS_TIMEOUT=15
    THREADS_TIMEOUT=12

    [SERVICES]
    DEFAULT_SERVICE=merge
    VIAS_MERGE=serial

    [PLUGINS]
    isbndb=isbndb.py
    openl=openl.py


The values are self-explanatory!


    **NOTE** If you are running ``isbntools`` inside a virtual environment, the
    ``isbntools.conf`` file will be at the root of the environment.

The easier way to manipulate these files is by using the script ``isbn_conf``.
At a terminal enter:

.. code-block:: bash

   $ isbn_conf show

to see the current conf file.

This script has many options that allow a controlled editing of the conf file.
Just enter ``isbn_conf`` for help.
