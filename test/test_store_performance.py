import unittest
import gc
import os
import itertools
import tempfile
from time import time
from random import random
from rdflib import Graph
from rdflib import URIRef


def random_uri():
    return URIRef("%s" % random())


class StoreTestCase(unittest.TestCase):
    """
    Test case for testing store performance... probably should be
    something other than a unit test... but for now we'll add it as a
    unit test.
    """
    store = 'IOMemory'
    path = None
    storetest = True
    performancetest = True

    def setUp(self):
        self.gcold = gc.isenabled()
        gc.collect()
        gc.disable()

        self.graph = Graph(store=self.store)
        fp, self.path = tempfile.mkstemp(suffix='.sqlite')
        self.graph.open(self.path, create=True)
        self.input = Graph()

    def tearDown(self):
        self.graph.close()
        if self.gcold:
            gc.enable()
        # TODO: delete a_tmp_dir
        self.graph.close()
        del self.graph
        if hasattr(self, 'path') and self.path is not None:
            if os.path.exists(self.path):
                if os.path.isdir(self.path):
                    for f in os.listdir(self.path):
                        os.unlink(self.path + '/' + f)
                    os.rmdir(self.path)
                elif len(self.path.split(':')) == 1:
                    os.unlink(self.path)
                else:
                    os.remove(self.path)

    def testTime(self):
        report = '"%s": [' % self.store
        for i in ['500triples', '1ktriples', '2ktriples',
                  '3ktriples', '5ktriples', '10ktriples',
                  '25ktriples']:
            inputloc = os.getcwd() + '/test/sp2b/%s.n3' % i
            res = self._testInput(inputloc)
            report += "%s," % res.strip()
        print(report + "],")

    def _testInput(self, inputloc):
        number = 1
        store = self.graph
        self.input.parse(location=inputloc, format="n3")

        def add_from_input():
            for t in self.input:
                store.add(t)
        it = itertools.repeat(None, number)
        t0 = time()
        for _i in it:
            add_from_input()
        t1 = time()
        return "%.3g " % (t1 - t0)

    def testQuery(self):
        query = """\
            PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX dc:      <http://purl.org/dc/elements/1.1/>
            PREFIX dcterms: <http://purl.org/dc/terms/>
            PREFIX bench:   <http://localhost/vocabulary/bench/>
            PREFIX xsd:     <http://www.w3.org/2001/XMLSchema#>

            SELECT ?yr
            WHERE {
              ?journal rdf:type bench:Journal .
              ?journal dc:title "Journal 1 (1940)"^^xsd:string .
              ?journal dcterms:issued ?yr
            }"""
        self.input.parse(location=os.getcwd() + '/test/sp2b/25ktriples.n3',
                        format="n3")
        t0 = time()
        res = self.input.query(query)
        t1 = time()
        print("Query time %s" % (t1 - t0))
        assert '1940' in str(list(res)[0])


class SQLiteStoreTestCase(StoreTestCase):
    store = "SQLite"

    def setUp(self):
        self.store = "SQLite"
        StoreTestCase.setUp(self)

if __name__ == '__main__':
    unittest.main()
