# tests/test_main.py
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import analyze_log  # Now this should work
import pytest

def test_analyze_log_errors():
    sample_logs = [
        "INFO: Started process",
        "WARNING: Disk space low",
        "ERROR: File not found"
    ]
    result = analyze_log(sample_logs)
    assert result['errors'] == 1
    assert result['warnings'] == 1

def test_analyze_log_no_errors():
    sample_logs = [
        "INFO: Everything OK",
        "INFO: Process complete"
    ]
    result = analyze_log(sample_logs)
    assert result['errors'] == 0
    assert result['warnings'] == 0
