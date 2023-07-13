# pylint:disable = protected-access
import types
import pytest
from cffconvert.cff_1_x_x.zenodo_author import ZenodoAuthor
from .get_every_key import get_every_key


@pytest.mark.parametrize("key", get_every_key())
def test_keys_zenodo_author(key):
    author = ZenodoAuthor(author=None)
    assert key in author._behaviors
    assert isinstance(author._behaviors[key], (types.MethodType, types.FunctionType))


def test_number_of_keys():
    expected = len(get_every_key())
    actual = len(ZenodoAuthor(author=None)._behaviors)
    assert actual == expected