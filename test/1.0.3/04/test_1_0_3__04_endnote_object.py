import os
from test.contracts.endnote_object import Contract
import pytest
from cffconvert import Citation
from cffconvert.behavior_1_0_x.endnote_object import EndnoteObject


@pytest.fixture(scope="module")
def endnote_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return EndnoteObject(citation.cffobj, initialize_empty=True)


class TestEndnoteObject(Contract):

    def test_as_string(self, endnote_object):
        actual_endnote = endnote_object.add_all().as_string()
        fixture = os.path.join(os.path.dirname(__file__), "endnote.enw")
        with open(fixture, "rt", encoding="utf-8") as f:
            expected_endnote = f.read()
        assert actual_endnote == expected_endnote

    def test_author(self, endnote_object):
        assert endnote_object.add_author().author == '%A Spaaks, Jurriaan H.\n%A Klaver, Tom\n' + \
                                                     '%A Verhoeven, Stefan\n%A Druskat, Stephan\n'

    def test_check_cffobj(self, endnote_object):
        endnote_object.check_cffobj()
        # doesn't need an assert

    def test_doi(self, endnote_object):
        assert endnote_object.add_doi().doi == '%R 10.5281/zenodo.1162057\n'

    def test_keyword(self, endnote_object):
        assert endnote_object.add_keyword().keyword == '%K citation\n%K bibliography\n%K cff\n%K CITATION.cff\n'

    def test_name(self, endnote_object):
        assert endnote_object.add_name().name == '%T cffconvert\n'

    def test_url(self, endnote_object):
        assert endnote_object.add_url().url == '%U https://github.com/citation-file-format/cff-converter-python\n'

    def test_year(self, endnote_object):
        assert endnote_object.add_year().year == '%D 2018\n'
