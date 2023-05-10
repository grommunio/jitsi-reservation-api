Jitsi reservation API
=====================

**The Jitsi reservation API complements grommunio Meet (and bare Jitsi) installations with a dual purpose API for creating room reservations and integrating these with newer installations of Jitsi using prosody-based room reservations**

|shield-agpl|_ |shield-release|_ |shield-loc|

.. |shield-agpl| image:: https://img.shields.io/badge/license-AGPL--3.0-green
.. _shield-agpl: LICENSE
.. |shield-release| image:: https://shields.io/github/v/tag/grommunio/jitsi-reservation-api
.. _shield-release: https://github.com/grommunio/jitsi-reservation-api/tags
.. |shield-loc| image:: https://img.shields.io/github/languages/code-size/grommunio/jitsi-reservation-api

At a glance
===========

* Provides REST API for room creation, validation and integration with grommunio
  Meet and any other Jitsi-based installation.

* Stores room reservation data in a sqlite database for data persistency

Built with
==========

* Python >= 3.6

* Python dependencies as per `</requirements.txt>`_

Getting started
===============

Prerequisites
-------------

* A working **grommunio Meet** or **Jitsi** installation

Installation
------------

* Install required packages listed in the `</requirements.txt>`_,
  either as system packages or in a virtual environment

* Deploy jitsi-reservation-api at a location of your choice, such as
  `/usr/share/jitsi-reservation-api`

* Customize configuration as needed

* Use `uwsgi` application server for service operation or use main.py for
  development run.

Support
=======

Support is available through grommunio GmbH and its partners. See
https://grommunio.com/ for details. A community forum is at
`<https://community.grommunio.com/>`_.

For direct contact and supplying information about a security-related
responsible disclosure, contact `dev@grommunio.com <dev@grommunio.com>`_.

Contributing
============

* https://docs.github.com/en/get-started/quickstart/contributing-to-projects

* Alternatively, upload commits to a git store of your choosing, or export the
  series as a patchset using `git format-patch
  <https://git-scm.com/docs/git-format-patch>`_, then convey the git
  link/patches through our direct contact address (above).
