import re
from cffconvert.cff_version_1_0_x.citation import Citation_1_0_x
from cffconvert.cff_version_1_1_x.citation import Citation_1_1_x
from cffconvert.cff_version_1_2_x.citation import Citation_1_2_x


class Citation:

    SUPPORTED_CFF_VERSIONS =                    \
        Citation_1_0_x.SUPPORTED_CFF_VERSIONS + \
        Citation_1_1_x.SUPPORTED_CFF_VERSIONS + \
        Citation_1_2_x.SUPPORTED_CFF_VERSIONS

    def __init__(self, cffstr):
        implementations = {
            "1.0.1": Citation_1_0_x,
            "1.0.2": Citation_1_0_x,
            "1.0.3": Citation_1_0_x,
            "1.1.0": Citation_1_1_x,
            "1.2.0": Citation_1_2_x,
        }
        cffversion = self._get_cff_version(cffstr)
        self._implementation = implementations[cffversion](cffstr, cffversion)

    @staticmethod
    def _get_cff_version(cffstr):
        res = re.search(r"^cff-version: ('|\")?(?P<cffversion>[\d\.]*)('|\")?.*", cffstr, re.MULTILINE)
        if res is None:
            raise ValueError("Unable to identify the schema version. Required key 'cff-version' seems to be missing.")
        cffversion = res.group("cffversion")
        if cffversion not in Citation.SUPPORTED_CFF_VERSIONS:
            raise ValueError("Unrecognized value for key \"cff-version\".")
        return cffversion

    # delegate method calls to the chosen implementation:
    def __getattr__(self, name):
        return getattr(self._implementation, name)
