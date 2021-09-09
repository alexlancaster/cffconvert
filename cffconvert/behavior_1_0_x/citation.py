import os
from pykwalify.core import Core
from ruamel.yaml import YAML
from cffconvert.behavior_1_0_x.apalike.apalike import ApalikeObject
from cffconvert.behavior_1_0_x.bibtex.bibtex import BibtexObject
from cffconvert.behavior_1_0_x.codemeta.codemeta import CodemetaObject
from cffconvert.behavior_1_0_x.endnote.endnote import EndnoteObject
from cffconvert.behavior_1_0_x.ris.ris import RisObject
from cffconvert.behavior_1_0_x.schemaorg.schemaorg import SchemaorgObject
from cffconvert.behavior_1_0_x.zenodo.zenodo import ZenodoObject
from cffconvert.contracts.citation import Contract
from cffconvert.root import get_package_root


class Citation_1_0_x(Contract):  # nopep8

    supported_cff_versions = [
        "1.0.1",
        "1.0.2",
        "1.0.3"
    ]

    def __init__(self, cffstr, cffversion):
        self.cffstr = cffstr
        self.cffversion = cffversion
        self.cffobj = self._parse()
        self.schema = self._get_schema()

    def _get_schema(self):
        schema_path = os.path.join(get_package_root(), "schemas", self.cffversion, "schema.yaml")
        with open(schema_path, "rt") as fid:
            return YAML(typ="safe").load(fid.read())

    def _parse(self):
        cffobj = YAML(typ="safe").load(self.cffstr)
        if not isinstance(cffobj, dict):
            raise ValueError("Provided CITATION.cff does not seem valid YAML.")
        return cffobj

    def as_apalike(self):
        return ApalikeObject(self.cffobj).print()

    def as_bibtex(self, reference='YourReferenceHere'):
        return BibtexObject(self.cffobj).print(reference)

    def as_cff(self):
        return self.cffstr

    def as_codemeta(self):
        return CodemetaObject(self.cffobj).print()

    def as_endnote(self):
        return EndnoteObject(self.cffobj).print()

    def as_ris(self):
        return RisObject(self.cffobj).print()

    def as_schemaorg(self):
        return SchemaorgObject(self.cffobj).print()

    def as_zenodo(self):
        return ZenodoObject(self.cffobj).print()

    def validate(self):
        # validation using YAML based schema
        Core(source_data=self.cffobj, schema_data=self.schema).validate(raise_exception=True)