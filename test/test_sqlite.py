import logging

_logger = logging.getLogger(__name__)

import test_context
import test_graph
from nose import SkipTest
from tempfile import mkdtemp

class SQLiteGraphTestCase(test_graph.GraphTestCase):
    storetest = True
    tmppath = mkdtemp()
    create = None
    def setUp(self):
        # self.store_name = "SQLite"
        # self.tmppath = mkdtemp()
        test_graph.GraphTestCase.setUp(self, self.tmppath)
    
    def tearDown(self):
        self.create = False
        test_graph.GraphTestCase.tearDown(self, self.tmppath)
   
    # def testStatementNode(self):
    #     raise SkipTest("Known issue.")

class SQLiteContextTestCase(test_context.ContextTestCase):
    storetest = True
    tmppath = mkdtemp()
    create = None
    def setUp(self):
        # self.store_name = "SQLite"
        # self.tmppath = mkdtemp()
        test_context.ContextTestCase.setUp(self, self.tmppath)

    def tearDown(self):
        self.create = False
        test_context.ContextTestCase.tearDown(self, self.tmppath)
   
    # def testConjunction(self):
    #     raise SkipTest("Known issue.")

    # def testContexts(self):
    #     raise SkipTest("Known issue.")

    # def testLenInMultipleContexts(self):
    #     raise SkipTest("Known issue.")


SQLiteGraphTestCase.storetest = True
SQLiteContextTestCase.storetest = True