import unittest
import os
import platform
from nose.exc import SkipTest
if platform.system() == 'Java':
    raise SkipTest("Skipping, too taxing for Jython")
import time
from glob import glob
from rdflib.graph import Graph
import tempfile

DEBUG = True
EVALUATE = True
DEBUG_PARSE = True
STORE = 'SQLite'
configString = ''
datasize = '1ktriples'


def create_graph(datafile):
    graph = Graph(store=STORE)
    fp, path = tempfile.mkstemp(suffix='.sqlite')
    graph.open(path, create=True)
    t1 = time.time()
    graph.parse(location=datafile, format='n3')
    t2 = time.time()
    print("%s loaded in %ss" % (datasize, t2 - t1))
    return graph

datafile = os.path.join(
            os.path.dirname(__file__), 'sp2b/' + datasize + '.n3')
the_graph = create_graph(datafile)

skiplist = [
    'q01',
    # 'q02',
    # 'q03a',
    # 'q03b',
    # 'q03c',
    'q04',
    # 'q05a',
    'q05b',
    'q06',
    'q07',
    'q08',
    # 'q09',
    # 'q10',
    # 'q11',
    # 'q12a',
    'q12b',
    # 'q12c',
]


class MetaRDFTest(type):
    def __new__(mcs, name, bases, dict):
        testfiles = glob(
                    os.path.join(os.path.dirname(__file__),
                    'sp2b/queries/*.sparql'))
        testfiles.sort()
        for test_name in testfiles:
            if test_name.split('/')[-1][:-7] not in skiplist:
                dict[test_name] = lambda self, test_name=test_name: \
                                                self.execute(test_name)
                # Doesn't look right in tracebacks, but looks fine in
                # nose output.
                dict[test_name].func_name = test_name
        return type.__new__(mcs, name, bases, dict)


class SQLiteTests(unittest.TestCase):
    __metaclass__ = MetaRDFTest

    def execute(self, testname):
        query = open(unicode(testname), 'r').read()
        t1 = time.time()
        result = the_graph.query(query, processor='sparql')
        # assert result == "not likely", result
        t2 = time.time()
        if getattr(result, 'result', False):
            if not result.result:
                def stab(result):
                    if result.askAnswer[0]:
                        return [True]
                    else:
                        []
                if result.askAnswer:
                    res = stab(result)
                else:
                    res = []
            else:
                res = result.result
        else:
            res = []
        print("%s : %s results in %fs" % (
            testname.split('/')[-1], len(res), t2 - t1))
