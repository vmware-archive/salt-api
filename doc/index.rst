========
salt-api
========

:command:`salt-api` is a modular interface on top of `Salt`_ that can provide a
variety of entry points into a running Salt system. It can start and manage
multiple interfaces allowing a REST API to coexist with XMLRPC or even a
Websocket API.

.. _`Salt`: http://saltstack.org/

Getting started
===============

1.  Install :command:`salt-api` on the same machine as your Salt master.
2.  Edit your Salt master config file for all required options for each netapi
    module you wish to run.
3.  Install any required additional libraries or software for each netapi
    module you wish to run.
4.  Run :command:`salt-api` which will then start all configured netapi
    modules.

.. note::

    Each ``netapi`` module will have differing configuration requirements and
    differing required software libraries.

    Exactly like the various module types in Salt (:term:`execution modules`,
    :term:`renderer modules`, :term:`returner modules`, etc.), :term:`netapi
    modules` in :program:`salt-api` will *not* be loaded into memory or started
    if all requirements are not met.

Development quickstart
======================

.. toctree::
    :maxdepth: 1

    topics/quickstart

Instalation
-----------------
1) Download and install cherrypy as a dependancy
2) Download salt-api and navigate to the folder
3) Install salt-api :command:`python setup.py install`
4) Run salt-api by issuing :command:`salt-api`

Configuration
-----------------
1) Setup `external_auth`_ in Salt master configuration file
2) Include the rest_cherrypy in your master configureation file::

   rest_cherrypy:
     port: 8000

     # Testing use only. Use SSL for production

     debug: True

.. _`external_auth`: http://docs.saltstack.org/en/latest/topics/eauth/index.html

netapi modules
==============

The core functionality for :command:`salt-api` lies in pluggable netapi modules
that adhere to the simple interface of binding to a port and starting a
service.

.. toctree::
    :maxdepth: 1

    topics/netapis/index
    topics/netapis/writing

Full list of netapi modules
---------------------------

.. toctree::
    :maxdepth: 2

    ref/netapis/all/index

Releases
========

.. toctree::
    :maxdepth: 1

    topics/releases/index

Reference
=========

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
* :ref:`glossary`
