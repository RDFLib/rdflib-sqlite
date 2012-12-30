import unittest
import tempfile
from rdflib import RDF
from rdflib import XSD
from rdflib.graph import ConjunctiveGraph

testgraph1 = """\
@prefix    : <http://example.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdf: <%s> .
:foo rdf:value "5.8"^^xsd:string .
:bar rdf:value "3" .
:gort rdf:value "4.8"^^xsd:string .""" % RDF.uri


testgraph2 = """\
@prefix    : <http://example.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdf: <%s> .
:foo rdf:value "5.8" .
:bar rdf:value "3" .
:gort rdf:value "4.8" .""" % RDF.uri


good_testquery = """
SELECT $node
WHERE {

    ?node rdf:value ?val .
    FILTER (?val < "4.7"^^xsd:string)
}"""


bad_testquery = """
SELECT ?node
WHERE {
    ?node rdf:value ?val .
    FILTER (?val < "4.7")
}"""


class TestIssue11(unittest.TestCase):
    debug = True

    def setUp(self):
        NS = u"http://example.org/"
        self.graph = ConjunctiveGraph(store="SQLite")
        fp, path = tempfile.mkstemp(suffix='.sqlite')
        self.graph.open(path, create=True)
        self.graph.parse(data=testgraph2, format="n3", publicID=NS)

    def testSPARQL_SQLite_lessthan_filter(self):
        rt = self.graph.query(good_testquery,
                initNs={'rdf': RDF, 'xsd': XSD}, DEBUG=True)
        # rt = self.graph.query(good_testquery, DEBUG=True)
        # assert str(list(rt)[0][0]) == "http://example.org/bar", list(rt)
        assert len(list(rt)) == 1, list(rt)

        # Counter-example demo
        rt = self.graph.query(bad_testquery,
                initNs={'rdf': RDF, 'xsd': XSD}, DEBUG=True)
        # rt = self.graph.query(bad_testquery, DEBUG=True)
        assert len(list(rt)) == 3, list(rt)
