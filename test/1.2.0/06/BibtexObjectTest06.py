import os
import pytest
from test.contracts.BibtexObject import Contract
from cffconvert import BibtexObject
from cffconvert import Citation


@pytest.fixture
def bibtex_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "r") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return BibtexObject(citation.cffobj, initialize_empty=True)


class BibtexObjectTest(Contract):

    def test_author(self, bibtex_object):
        bibtex_object.add_author()
        assert bibtex_object.author == 'author = {Jurriaan H. Spaaks and Tom Klaver}'

    def test_check_cff_object(self, bibtex_object):
        bibtex_object.check_cff_object()
        # doesn't need an assert

    def test_doi(self, bibtex_object):
        bibtex_object.add_doi()
        assert bibtex_object.doi == 'doi = {10.5281/zenodo.1162057}'

    def test_month(self, bibtex_object):
        bibtex_object.add_month()
        assert bibtex_object.month == 'month = {1}'

    def test_print(self, bibtex_object):
        actual_bibtex = bibtex_object.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "bibtex.bib")
        with open(fixture, "r") as f:
            expected_bibtex = f.read()
        assert actual_bibtex == expected_bibtex

    def test_title(self, bibtex_object):
        bibtex_object.add_title()
        assert bibtex_object.title == 'title = {cff-converter-python}'

    def test_url(self, bibtex_object):
        bibtex_object.add_url()
        assert bibtex_object.url == 'url = {https://github.com/citation-file-format/cff-converter-python}'

    def test_year(self, bibtex_object):
        bibtex_object.add_year()
        assert bibtex_object.year == 'year = {2018}'
