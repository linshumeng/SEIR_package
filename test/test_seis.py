"""Tests for seis model."""

import os

def test_path():
    """Theck whether the .py exists."""
    assert os.path.exists("src/seis/seis.py")