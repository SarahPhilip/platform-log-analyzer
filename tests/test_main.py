import pytest
import sys
import os

# Add project root to path so main.py can be imported
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import analyze_log


def test_valid_file_returns_list():
    errors = analyze_log("sample.log")
    assert isinstance(errors, list)


def test_only_error_lines_returned():
    errors = analyze_log("sample.log")
    assert all("ERROR" in e for e in errors)


def test_empty_file():
    errors = analyze_log("empty.log")
    assert errors == []


def test_no_error_file():
    errors = analyze_log("noerror.log")
    assert len(errors) == 0


def test_missing_file():
    with pytest.raises(SystemExit):
        analyze_log("missing.log")

