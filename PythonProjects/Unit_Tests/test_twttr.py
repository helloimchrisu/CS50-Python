import pytest
from twttr import shorten

def test_hello():
    assert shorten("hello") == ("hll")
