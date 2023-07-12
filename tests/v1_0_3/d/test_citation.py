import datetime
import os
from cffconvert.citation import Citation


def citation():
    p = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(p, "rt", encoding="utf-8") as fid:
        cffstr = fid.read()
        return Citation(cffstr)


def test_cffobj():
    assert isinstance(citation().cffobj["date-released"], datetime.date)
    assert citation().cffobj["date-released"] == datetime.date(year=2018, month=7, day=25)


def test_cffversion():
    assert citation().cffversion == "1.0.3"


def test_validate():
    citation().validate()
