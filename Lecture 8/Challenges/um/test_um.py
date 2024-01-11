import pytest
from um import count

def test_default():
    assert count("um") == 1
    assert count("um?") == 1

def test_spaces():
    assert count("Um, thanks for the album.") == 1

def test_words():
    assert count("Um, thanks, um...") == 2
