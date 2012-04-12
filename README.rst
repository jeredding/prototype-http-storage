=======================
HTTP Storage Prototype
=======================

Purpose
=======

This prototype is intended to act as a proof of concept for a RESTful web
service that provides an interface to an underlying file system. The goal is
to have a daemon process that can watch a directory tree and consistently
identify files as both their contents and their locations within the directory
tree change. The current state of any particular file will be made available
to a web service through some form of database. The web service will provide
an API that allows clients to download files from the directory tree in
variable sized chunks that can be authenticated using a hashing algorithm.

Implementation
==============

FS Daemon
---------

The daemon process that watches for changes within the directory tree will be
driven by the `PyInotify library <https://github.com/seb-m/pyinotify>`_.
Should the PyInotify library prove insufficient, the 
`Watchdog library <https://github.com/gorakhargosh/watchdog>`_ will be tested.
For the purposes of this prototype, the daemon process will not expose any
type of API. Instead it will simply keep a local SQLite database updated for
use by the web service.

File Database
-------------

The database for this prototype will simply be a local SQLite names `files.db`.
This database will have a simplified schema consisting of a single table
called `files` with the following schema:

+--------+-----------+----------------------------------------------+
| Name   | Type      | Details                                      |
+========+===========+==============================================+
| id     | TEXT      | A UUID4 that identifies the file.            |
+--------+-----------+----------------------------------------------+
| hash   | BLOB      | A SHA256 hash that verifies the file.        |
+--------+-----------+----------------------------------------------+
| path   | TEXT      | The path relative to the watched directory.  |
+--------+-----------+----------------------------------------------+

This schema is designed for small scale tests only.

Web Service
-----------

`Web.py <https://github.com/webpy/webpy>`_ will provide the basis for the REST
service. For the purposes of this prototype, the service will expose a single
resource named `File` and a single verb of `GET`. The service will accept
standard HTTP `Range` headers as valid parameters for delivering file chunks.
Each chunk will be delivered with a validation hash in a custom response
header named `Application-Validation-Hash`.

Development Process
-------------------

Development will follow the following progression:

1. Skeleton code generation

2. Docstring generation

3. Unit test generation

4. Implementation

Standards
=========

Commits
-------

All commit messages should follow the guide
`here <http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html>`_
that describes the general structure of a good commit message. Adding to the
standards listed in the guide, the following standards should also be followed:

1. All messages begin with a verb in the imperative sense.

2. Limit verbs to `Add`, `Fix`, `Change`, `Remove`.

3. Place a colon (`:`) after the verb. `Add:`, `Fix:`, etc.

4. Make sure every commit is signed using `--signoff`.

If struggling for a good commit message just ask what the patch would do if
installed. Would it *Add: Feature X* or *Fix: Issue #00000*?


Docstrings
----------

Docstrings should use the following pattern:

.. code-block:: python

    """One line description of function/class.

    Extended description of input requirements.

    Extended description of output specifications.
    """

All functions and classes should be documented in using this pattern prior to
code implementation.

Unit Tests
----------

This project will make use of the `unittest` Python module for unit testing.
Unit tests should take place in two phases.

1. Pre-Implementation Phase

    The first unit tests should be written prior to code implementation. The
    unit tests should be written to test any input or output specification
    defined in the docstring of the unit being tested. This should be the
    equivalent of a black-box testing.

2. Post-Implementation Phase

    After code implementation unit tests should be expanded to test potential
    problem areas in specific to the logic used in implementation. This should
    be the equivalent of white-box testing.
