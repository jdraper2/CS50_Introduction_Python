import pytest
from numb3rs import validate

def test_default():
    assert validate("127.0.1.2") == True

def test_range():
    assert validate("127.0.1.275") == False
    assert validate("512.512.512.512") == False

def test_str():
    assert validate("cat") == False
