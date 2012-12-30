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


Usage
=====

The modern way - by specifying "SQLite" as the first positional argument
to Graph(), e.g.

.. code-block:: python

    from rdflib import Graph
    g = Graph('SQLite')
    g.open('/path/to/sqlite/file', create=True)


The traditional way - create a store and then provide the store as the
first positional argument to Graph(), e.g.

.. code-block:: python

    from rdflib import plugin, Store, Graph
    store = plugin.get('SQLite', Store)('rdfstore')
    store.open('/path/to/sqlite/file', create=True)
    g = Graph(store)


Code sample
-----------

.. code-block:: pycon

    >>> import os
    >>> from rdflib import ConjunctiveGraph, URIRef
    >>> 
    >>> default_graph_uri = URIRef("http://rdflib.net/data")
    >>> configString = "testdata.sqlite"
    >>> 
    >>> g = ConjunctiveGraph('SQLite', identifier=default_graph_uri)
    >>> 
    >>> g.open(configString, create=True)
    1
    >>> print(g)
    [a rdflib:ConjunctiveGraph;rdflib:storage
                            [a rdflib:Store;rdfs:label 'SQLite']]
    >>> 
    >>> print(g.store)
    <Partitioned SQL N3 Store:
        0 contexts, 0 classification assertions,
        0 quoted statements, 0 property/value assertions,
        and 0 other assertions>
    >>> 
    >>> print(g.identifier)
    http://rdflib.net/data
    >>> 
    >>> g.close()
    >>> os.unlink(os.getcwd() + '/' + configString)


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
