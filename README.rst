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


ATTENTION Users
---------------

This software is not usable at the moment. Please be patient and stand by until
the first release. Thank you!

Description
-----------

Functions to add tasks, projects and checklists on OS X to the
`2DoApp <http://www.2doapp.com>`_ from the command line.

Since version 1.5 (Mac) 2Do supports adding tasks by using an URL scheme.

If you want to add a task, you can open the URL::

    twodo://x-callback-url/add?task=Save%20the%20world

The task ``Save the world`` will be added to your default list.

* Free software: ISC license

.. Documentation: https://twodolib.readthedocs.org.

Features
--------

* Create tasks on the command line and show the corresponding URL scheme, for
  copy and pasting it.
* Create tasks on the command line and open the corresponding URL scheme.

