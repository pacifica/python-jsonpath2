.. Pacifica Policy documentation master file, created by
   sphinx-quickstart on Thu Dec  6 20:05:08 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Pacifica Policy's documentation!
=============================================

The Pacifica Policy service provides endpoints that define policy
questions for institutions. This is separate from other services as
certain operations required by other Pacifica Core services are more
Policy base.

Practially speaking, when the question a Pacifica service wants to
ask the Metadata service is sufficiently complex it should really be
a Policy question. For example, when uploading data the ingest
service needs to validate the metadata requesting to be added. This
new metadata needs to be verified by some institutional requirements.
So there is a Policy endpoint (several actually) that help ensure
those requirements are met.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   exampleusage
   jsonpath2

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
