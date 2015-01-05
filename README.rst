========
salt-api
========

The ``salt-api`` project `has been merged into the main Salt repository as
of Salt's 2014.7 release`__.

.. __: http://docs.saltstack.com/en/latest/topics/releases/2014.7.0.html#salt-api-project-merge

We recommend installing salt-api using a package manager as usual. Some
distributions (RHEL/Cent) have split packages and so the package name will be
``salt-api`` and require a separate install. Some distributions do not split
packages and it will be bundled within the ``salt-master`` package.

Verify which version you have installed by running ``salt-api --version``; if
the version number does not start with ``2014`` you are running an old release.

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
