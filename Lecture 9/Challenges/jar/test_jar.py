import pytest
from jar import Jar


def test_1():
    test1_jar = Jar(12)
    assert test1_jar.capacity == 12

def test_2():
    test2_jar = Jar(12)
    test2_jar.deposit(4)
    assert test2_jar.size == 4

def test_3():
    test3_jar = Jar(12)
    test3_jar.deposit(4)
    test3_jar.withdraw(2)
    assert test3_jar.size == 2

def test_4():
    with pytest.raises(ValueError):
        test4_jar = Jar(-1)
