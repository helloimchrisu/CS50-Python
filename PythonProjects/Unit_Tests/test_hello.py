from hello_with_test import hello

def test_default():
    assert hello() == "hello, world"

def test_david():
    assert hello("David") == "hello, David"

    