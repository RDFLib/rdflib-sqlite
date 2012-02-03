from setuptools import setup

setup(
    name = 'rdflib-store-sqlite',
    version = '0.1',
    description = "rdflib extension adding SQLite as back-end store",
    author = "Graham Higgins",
    author_email = "gjhiggins@gmail.com",
    url = "http://github.com/RDFLib/rdflib-store-sqlite",
    py_modules = ["rdflib_sqlite"],
    test_suite = "test",
    install_requires = ["rdflib>=3.0", "rdfextras>=0.1"],
    entry_points = {
    	'rdf.plugins.store': [
            'SQLite = rdfextras.store.SQLite:SQLite',
        ],
    }

)
