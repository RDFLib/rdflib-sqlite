import logging

_logger = logging.getLogger(__name__)

import context_case
import graph_case
from nose import SkipTest
from rdflib import URIRef
from tempfile import mkstemp

"""
Note: identifier must be a URIRef, choosing to use a Literal causes
a "KeyError" exception when term2Letter() is called:

======================================================================
ERROR: testAdd (test.test_sqlite.SQLiteGraphTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File ".../rdflib-sqlite/test/graph_case.py", line 77, in testAdd
    self.addStuff()
  File ".../rdflib-sqlite/test/graph_case.py", line 50, in addStuff
    self.graph.add((tarek, likes, pizza))
  File ".../rdflib/graph.py", line 349, in add
    self.__store.add((s, p, o), self, quoted=False)
  File ".../rdflib-sqlite/rdflib_sqlite/AbstractSQLStore.py", line 522, in add
    subject, predicate, obj, context, self._internedId, quoted)
  File ".../rdflib-sqlite/rdflib_sqlite/AbstractSQLStore.py", line 299, in buildTripleSQLCommand
    triplePattern = statement2TermCombination(subject, predicate, obj, context)
  File ".../rdfextras/utils/termutils.py", line 204, in statement2TermCombination
    term2Letter(obj), normalizeGraph(context)[-1])]
KeyError: 'UUUL'
"""

class SQLiteGraphTestCase(graph_case.GraphTestCase):
    storetest = True
    fp, tmppath = mkstemp(prefix='test',dir='/tmp')
    create = True
    store_name = "SQLite"
    identifier = URIRef("http://rdflib.net")

    def setUp(self):
        graph_case.GraphTestCase.setUp(self)
    
    def tearDown(self):
        graph_case.GraphTestCase.tearDown(self)
   
    def testStatementNode(self):
        raise SkipTest("Known issue.")

class SQLiteContextTestCase(context_case.ContextTestCase):
    storetest = True
    fp, tmppath = mkstemp(prefix='test',dir='/tmp')
    create = True
    store_name = "SQLite"
    identifier = URIRef("http://rdflib.net")

    def setUp(self):
        context_case.ContextTestCase.setUp(self)

    def tearDown(self):
        self.create = False
        context_case.ContextTestCase.tearDown(self)
   
    def testConjunction(self):
        raise SkipTest("Known issue.")

    def testContexts(self):
        raise SkipTest("Known issue.")

    def testLenInMultipleContexts(self):
        raise SkipTest("Known issue.")


SQLiteGraphTestCase.storetest = True
SQLiteContextTestCase.storetest = True

