import pytest
from ..hangman.hangman import Hangman


def test_to_str():
    h = Hangman()
    lst = ['a', 'b', 'c']
    result = h.to_str(lst)
    assert result == 'abc'
