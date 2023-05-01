import pytest
from utils.dicts import get_val


def test_get_val():
    assert get_val({"vcs": "mercurial"}, "vcs") == "mercurial"
    assert get_val({"vcs": "mercurial"}, "vcs", "git") == "mercurial"
    assert get_val({"vcs": "mercurial"}, "mercurial") == "git"
    assert get_val({}, "vcs", "git") == "git"
    assert get_val({}, "vcs", "bazaar") == "bazaar"
    assert get_val([1, 2, 3, 4], 2, "bazar") == "bazar"
