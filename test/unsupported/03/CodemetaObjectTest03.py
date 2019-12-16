from cffconvert import CodemetaObject
import unittest
import os
import ruamel.yaml as yaml


class CodemetaObjectTest(unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
            cff_object = yaml.safe_load(cffstr)
            self.co = CodemetaObject(cff_object, initialize_empty=True)

    def test_check_cff_object(self):
        with self.assertRaises(ValueError) as context:
            self.co.check_cff_object()
        self.assertTrue('Missing key "cff-version" in CITATION.cff file.' in str(context.exception))
