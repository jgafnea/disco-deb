import gzip
from collections import Counter
from unittest.mock import Mock, patch

import pytest
import requests

from app import BASE_URL, get_contents, get_counts, show_top

# First are tests for the happy path.


@patch("requests.get")
def test_get_contents_200(mock_get):
    """Test `get_contents` with a successful response."""

    # Mock the 200 response.
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = gzip.compress(b"valid contents")
    mock_get.return_value = mock_response

    # Call real function and check the results.
    actual = get_contents("amd64")
    expected = "valid contents"
    assert actual == expected
    mock_get.assert_called_once_with(f"{BASE_URL}/Contents-amd64.gz")


@pytest.fixture
def mock_contents():
    return """
bin/file1 packageA
bin/file2 packageA,packageB
bin/file3 packageA,packageB,packageC
MALFORMED/FILE/PACKAGE
"""


def test_get_counts_200(mock_contents):
    """Test `get_counts` showing correct counts."""
    result = get_counts(mock_contents)
    expected = Counter({"packageA": 3, "packageB": 2, "packageC": 1})
    assert result == expected


def test_show_top_200(mock_contents, capsys):
    """Test `show_top` showing correct top result."""
    result = get_counts(mock_contents)
    show_top(result)
    captured = capsys.readouterr()
    assert "01. packageA" in captured.out
    assert "" in captured.err


# Below are tests for the edge cases.


@patch("requests.get")
def test_get_contents_404(mock_get):
    """Test `get_contents` with a failed response."""

    # Mock the 404 response.
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    # Call real function and check the results.
    actual = get_contents("amd64")
    expected = None
    assert actual == expected
    mock_get.assert_called_once_with(f"{BASE_URL}/Contents-amd64.gz")


def test_get_counts_404():
    """Test `get_counts` of None."""
    result = get_counts(None)
    expected = Counter()
    assert result == expected


def test_show_top_404(capsys):
    """Test `show_top` of empty counter."""
    result = get_counts(None)
    show_top(result)
    captured = capsys.readouterr()
    assert "" in captured.out
    assert "" in captured.err
