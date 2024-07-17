import pytest
from bank import value

def test_hello_upper():
    assert value("Hello") == 0
def test_hello_lower():
    assert value("hello") == 0
def test_hi():
    assert value("hi") == 20
def test_aaa():
    assert value("aaa") == 100