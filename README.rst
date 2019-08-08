=====================
ZODB Research Project
=====================

In September 2019, before PyColorado, I'm sprinting with Jim to learn
some patterns about ZODB, pseudo-reactive programming, generational
sets, references, high performance collections, etc.

See `Questions <QUESTIONS.RST>`_ for research topics I've come up with.

Install
=======

Requires Python 3.7+

#. ``pip install -e .`` or ``python setup.py develop``

#. ``python -m jimfulton_research.watch`` goes into "server" mode, so
   to speak. See below.

#. ``python -m jimfulton_research.dump`` gives a listing of some of the
   ZODB content. Since we're not doing ZEO at the moment, can't run at
   same time as ``watch``.

Exploring the Code
==================

``bootstrap.py`` is the main driver. It:

- Makes a database and a root with sample content, if needed

- Makes an instance of the threadwatcher (though doesn't start it, the
  ``watcher/__main__.py`` console script starts it up)

- Subscribes to changeset events fired by ``notify`` in the thread

Watch Mode
==========

This runs a thread which uses the code in ``directory_watcher``. Basic
premise:

- The ``process_filesystem`` method walks the directory structure using
  the very-fast ``os.scandir`` from modern Python

- Files changed since the last interval are gathered into a "ChangeSet"
  of add/edit/delete info

- A callback is run with that info provided

- Sleep for an interval, start again

The current callback uses ``zope.event`` to broadcast the ChangeSet to
subscribers. Since the notify happens in a subthread, the hope is that the
subscribers run in the main thread and write to the ZODB.
