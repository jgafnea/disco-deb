from collections import Counter

import pytest

from app import get_counts, show_top


@pytest.fixture
def contents():
    return """
bin/file1 packageA
bin/file2 packageA,packageB
bin/file3 packageA,packageB,packageC
MALFORMED/FILE/PACKAGE
"""


def test_get_counts(contents):
    """Test `get_counts` showing correct counts and handling malformed line."""
    counts = get_counts(contents)
    expected = Counter({"packageA": 3, "packageB": 2, "packageC": 1})
    assert counts == expected


def test_show_top(contents, capsys):
    """Test `show_top` showing expected output and no errors."""
    counts = get_counts(contents)
    show_top(counts, number=3)
    captured = capsys.readouterr()
    assert "01. packageA" in captured.out
    assert "" in captured.err
