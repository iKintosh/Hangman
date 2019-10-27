from ..hangman.hangman import Hangman


def test_to_str():
    hang = Hangman()
    lst = ['a', 'b', 'c']
    result = hang.to_str(lst)
    assert result == 'abc'
