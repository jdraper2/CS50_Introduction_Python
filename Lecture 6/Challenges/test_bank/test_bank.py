import pytest
from bank import value

def test_default():
    assert value("Hello") == "$0"


def test_Hgrettings():
    assert value("Hi") == "$20"
    assert value("how are you") == "$20"

def test_payout():
    assert value("What's Up") == "$100"