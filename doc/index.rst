========
salt-api
========

The ``salt-api`` project `has been merged`__ into the main Salt repository as
of Salt's **Helium** release.

.. __: https://github.com/saltstack/salt/pull/13554

No api changes were made. The ``salt-api`` daemon remains intact and is
now available in the default ``salt-master`` install.

The documentation has been moved into the main salt project as well. ``netapi``
module documentation is available in the module index.

No further development will take place in this repository. It will be left in
the current state for historical purposes. Open issues will be migrated to the
Salt repository.

Documentation
=============

The documentation now lives within the main Salt documentation.

* `Introduction to netapi modules
  <http://docs.saltstack.com/en/latest/topics/netapi/index.html>`_
* `Full list of netapi modules
  <http://docs.saltstack.com/en/latest/ref/netapi/all/index.html>`_
* `Archived release notes
  <http://docs.saltstack.com/en/latest/topics/releases/saltapi/index.html>`_

======================
Archived Documentation
======================

The documentation for the final salt-api release, 0.8.4.1, is included below.

----------

:program:`salt-api` is a modular interface on top of `Salt`_ that can provide a
variety of entry points into a running Salt system. It can start and manage
multiple interfaces allowing a REST API to coexist with XMLRPC or even a
Websocket API.

.. _`Salt`: http://saltstack.org/

Getting started
===============

1.  Install :program:`salt-api` on the same machine as your Salt master.
2.  Edit your Salt master config file for all required options for each
    ``netapi`` module you wish to run.
3.  Install any required additional libraries or software for each ``netapi``
    module you wish to run.
4.  Run :command:`salt-api` which will then start all configured ``netapi``
    modules.

.. note::

    Each ``netapi`` module will have differing configuration requirements and
    differing required software libraries.

    Exactly like the various module types in Salt (:term:`execution modules`,
    :term:`renderer modules`, :term:`returner modules`, etc.), :term:`netapi
    modules` in :program:`salt-api` will *not* be loaded into memory or started
    if all requirements are not met.

Installation quickstart
=======================

.. toctree::
    :maxdepth: 1

    topics/quickstart

``netapi`` modules
==================

The core functionality for :program:`salt-api` lies in pluggable ``netapi``
modules that adhere to the simple interface of binding to a port and starting a
service. :program:`salt-api` can manage one or many services concurrently.

Full list of ``netapi`` modules
-------------------------------

.. toctree::
    :maxdepth: 3

    ref/netapis/all/index

``netapi`` developer reference
------------------------------

.. toctree::
    :maxdepth: 1

    topics/netapis/index
    topics/netapis/writing

Releases
========

.. toctree::
    :maxdepth: 2

    topics/releases/index

Reference
=========

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
* :ref:`glossary`
