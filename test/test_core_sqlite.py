import unittest
import os
import tempfile
from rdflib import Graph
from rdflib import Literal
from rdflib import URIRef
from rdflib.namespace import XSD, RDFS
from rdflib.py3compat import b


class CoreSQLiteStoreTestCase(unittest.TestCase):
    """
    Test case for SQLite core.
    """
    store = "SQLite"
    path = None
    storetest = True

    def setUp(self):
        self.graph = Graph(store=self.store)
        fp, self.path = tempfile.mkstemp(suffix='.sqlite')
        self.graph.open(self.path, create=True)

    def tearDown(self):
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

    def test_escape_quoting(self):
        test_string = "This's a Literal!!"
        self.graph.add(
            (URIRef("http://example.org/foo"),
             RDFS.label,
             Literal(test_string, datatype=XSD.string)))
        self.graph.commit()
        assert b("This's a Literal!!") in self.graph.serialize(format="xml")

if __name__ == '__main__':
    unittest.main()
