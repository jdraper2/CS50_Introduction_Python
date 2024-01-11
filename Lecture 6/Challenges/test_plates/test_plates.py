import pytest
from plates import is_valid

def test_default():
    assert is_valid("AAA111") == True

def test_len():
    assert is_valid("A") == False
    assert is_valid("AAA1234") == False
    assert is_valid("AAA123") == True
    assert is_valid("AA") == True

def test_aplphabet():
    assert is_valid("123") == False

def test_order():
    assert is_valid("AA2A") == False

def test_zero():
    assert is_valid("AAA012") == False
    assert is_valid("AAA102") == True

def test_special_char():
    assert is_valid("AA--") == False
