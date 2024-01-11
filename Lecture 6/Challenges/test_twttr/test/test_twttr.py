from twttr import shorten
import pytest

def test_default():
    assert shorten("Hello") == "Hll"

def test_case():
    assert shorten("Hello World") == "Hll Wrld"
    assert shorten("hello world") == "hll wrld"
    assert shorten("HELLO WORLD") == "HLL WRLD"

def test_mnumber_inputs():
    assert shorten("Hello 123") == "Hll 123"

def test_punctuation():
    assert shorten("hello, world") == "hll, wrld"
