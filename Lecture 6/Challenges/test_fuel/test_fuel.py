import pytest
from fuel import convert, gauge

def test_default_convert():
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("4/4") == 100

def test_str_convert():
    with pytest.raises(ValueError):
        convert("cat")

def test_fail_convert():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")
    with pytest.raises(ValueError):
        convert("5/4")

def test_str_guage():
    assert gauge(1) == "E"
    assert gauge(100) =="F"
    assert gauge(75) == "75%"
