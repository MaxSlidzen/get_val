import pytest
from utils.dicts import get_val


@pytest.fixture
def get_array():
    return {"vcs": "mercurial"}


def test_get_val_1(get_array):
    assert get_val(get_array, "vcs") == "mercurial"
    assert get_val(get_array, "vcs", "git") == "mercurial"
    assert get_val(get_array, "mercurial") == "git"


@pytest.mark.parametrize("a, b, c, res", [({}, "vcs", "git", "git"),
                                          ({}, "vcs", "bazaar", "bazaar"),
                                          ([1, 2, 3, 4], 2, "bazar", "bazar"),
                                          ])
def test_get_val_2(a, b, c, res):
    assert get_val(a, b, c) == res
    # assert get_val({}, "vcs", "bazaar") == "bazaar"
    # assert get_val([1, 2, 3, 4], 2, "bazar") == "bazar"
