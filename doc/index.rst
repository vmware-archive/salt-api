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

Running :command:`salt-api` will automatically start any netapi modules that
have been configured in your Salt master config file. Consult the documentation
for each netapi module for what options are required. :command:`salt-api` must
be run on the same machine as your Salt master.

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
