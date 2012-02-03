from rdflib import plugin
from rdflib import store
from rdflib import query
#from .test_context import ContextTestCase
#from .test_graph import GraphTestCase

import sys # sop to Hudson
sys.path.insert(0, '/var/lib/tomcat6/webapps/hudson/jobs/rdfextras')

plugin.register(
        'SQLite', store.Store,
        'rdfextras.store.SQLite', 'SQLite')

