import pytest
from seasons import birth_date
from datetime import date
from datetime import timedelta

def test_1():
    assert birth_date(str(date.today()-timedelta(days=365))) == "Five hundred twenty-five thousand, six hundred minutes"
    assert birth_date(str(date.today()-timedelta(days=730))) == "One million, fifty-one thousand, two hundred minutes"

def test_2():
    assert birth_date("2023 10 01") == "Invalid Date"
