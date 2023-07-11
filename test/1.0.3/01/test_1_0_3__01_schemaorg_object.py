import os
from test.contracts.schemaorg_object import Contract
import pytest
from cffconvert import Citation
from cffconvert.behavior_1_0_x.schemaorg_object import SchemaorgObject


@pytest.fixture(scope="module")
def schemaorg_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return SchemaorgObject(citation.cffobj, initialize_empty=True)


class TestSchemaorgObject(Contract):

    def test_as_string(self, schemaorg_object):
        actual_schemaorg = schemaorg_object.add_all().as_string()
        fixture = os.path.join(os.path.dirname(__file__), "schemaorg.json")
        with open(fixture, "rt", encoding="utf-8") as f:
            expected_schemaorg = f.read()
        assert actual_schemaorg == expected_schemaorg

    def test_author(self, schemaorg_object):
        assert schemaorg_object.add_author().author == [{
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "legalName": "Netherlands eScience Center"
            },
            "familyName": "Spaaks",
            "givenName": "Jurriaan H.",
            "email": "my@email.notexist"
        }, {
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "legalName": "Netherlands eScience Center"
            },
            "familyName": "Klaver",
            "givenName": "Tom"
        }]

    def test_check_cffobj(self, schemaorg_object):
        schemaorg_object.check_cffobj()
        # doesn't need an assert

    def test_code_repository(self, schemaorg_object):
        assert schemaorg_object.add_urls().code_repository == 'https://github.com/citation-file-format' + \
                                                              '/cff-converter-python'

    def test_date_published(self, schemaorg_object):
        assert schemaorg_object.add_date_published().date_published == '2018-01-16'

    def test_description(self, schemaorg_object):
        assert schemaorg_object.add_description().description is None

    def test_identifier(self, schemaorg_object):
        assert schemaorg_object.add_identifier().identifier == 'https://doi.org/10.5281/zenodo.1162057'

    def test_keywords(self, schemaorg_object):
        assert schemaorg_object.add_keywords().keywords == ['citation', 'bibliography', 'cff', 'CITATION.cff']

    def test_license(self, schemaorg_object):
        assert schemaorg_object.add_license().license == 'https://spdx.org/licenses/Apache-2.0'

    def test_name(self, schemaorg_object):
        assert schemaorg_object.add_name().name == 'cff-converter-python'

    def test_url(self, schemaorg_object):
        assert schemaorg_object.add_urls().url == 'https://github.com/citation-file-format' + \
                                                  '/cff-converter-python'

    def test_version(self, schemaorg_object):
        assert schemaorg_object.add_version().version == '1.0.0'
