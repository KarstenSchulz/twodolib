======================================================
twodolib - A commandline helper to add tasks to 2DoApp
======================================================


.. image:: https://img.shields.io/github/release/KarstenSchulz/twodolib.svg
    :target: https://github.com/KarstenSchulz/twodolib/releases

.. image:: https://img.shields.io/travis/KarstenSchulz/twodolib.svg
    :target: https://travis-ci.org/KarstenSchulz/twodolib

.. image:: https://img.shields.io/coveralls/KarstenSchulz/twodolib.svg
    :target: https://coveralls.io/github/KarstenSchulz/twodolib?branch=master

.. image:: https://img.shields.io/requires/github/KarstenSchulz/twodolib.svg
    :target: https://requires.io/github/KarstenSchulz/twodolib/requirements/?branch=master

.. image:: https://img.shields.io/pypi/v/twodolib.svg
    :target: https://pypi.python.org/pypi/twodolib

.. image:: https://img.shields.io/github/license/KarstenSchulz/twodolib.svg
    :target: https://opensource.org/licenses/ISC


Description
-----------

This package provides the library ``twodolib`` and a command line utility
``task2do`` to add tasks, projects and checklists to the macOS App
`2DoApp <http://www.2doapp.com>`_ from the command line.

Since version 1.5 (Mac) 2Do supports adding tasks by using an URL scheme.
For example, if you want to add the task *Save the world.*, you can open the
URL::

    twodo://x-callback-url/add?task=Save%20the%20world.

to add this task to your 2Do App (see: https://www.2doapp.com/kb/article/url-schemes.html)

The ``task2do`` command supports creating such URLs from the command line.
To print such an URL for a task without adding it, just enter::

    task2do "Save the world."

which prints the URL to stdout like this::

    twodo://x-callback-url/add?task=Save%20the%20world.

If you want to actually add the task to your 2Do App, use the ``-e`` or
``--execute`` option::

        task2do -e "Save the world."
        # no output here, but the task should be added into your standard list in 2Do

Features
--------

* runs with Python 3 and Python 2
* Create tasks on the command line and show the corresponding URL scheme, for copy and pasting it.
* Create tasks on the command line and open the corresponding URL scheme to send it to `2DoApp <http://www.2doapp.com>`_

See the documentation at http://twodolib.readthedocs.org/en/latest/

Install
-------

See `docs/installation.rst <https://github.com/KarstenSchulz/twodolib/blob/master/docs/installation.rst>`_
(It's just ``pip install twodolib``)


Dependencies
------------

* wheel

License
-------

* Free software: ISC license

.. Documentation: https://twodolib.readthedocs.org.

