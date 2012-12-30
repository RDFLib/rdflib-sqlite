.. rdflib-sqlite documentation master file

================================================================
RDFLib-SQLite :: a formula-aware Store based on AbstractSQLStore
================================================================

A SQLite RDFLib store formula-aware implementation.

It stores its triples in the following partitions:

* Asserted non rdf:type statements
* Asserted rdf:type statements (in a table which models Class membership). The motivation for this partition is primarily query speed and scalability as most graphs will always have more rdf:type statements than others
* All Quoted statements

In addition it persists namespace mappings in a separate table

Contents:

.. toctree::
   :maxdepth: 2

Module API
++++++++++

.. currentmodule:: rdflib_sqlite.SQLite

:mod:`rdflib_sqlite.SQLite`
----------------------------------------
.. automodule:: rdflib_sqlite.SQLite
.. autoclass:: SQLite
   :members:
.. autofunction:: regexp


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
