### NOTE - this code is not maintained, and not guaranteed to work with newer versions of rdflib!

For RDBMS based persistence for RDFLib we recommend you use 

https://github.com/RDFLib/rdflib-sqlalchemy

---


=============
RDFLib-SQLite
============= 

A SQLite RDFLib store formula-aware implementation.

It stores its triples in the following partitions:

- Asserted non rdf:type statements
- Asserted rdf:type statements (in a table which models Class membership)
  The motivation for this partition is primarily query speed and scalability
  as most graphs will always have more rdf:type statements than others
- All Quoted statements

In addition it persists namespace mappings in a separate table.

[![Build Status](https://travis-ci.org/RDFLib/rdflib-sqlite.png?branch=master)](https://travis-ci.org/RDFLib/rdflib-sqlite)
