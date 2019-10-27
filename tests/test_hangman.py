from ..hangman.hang_man import Hang_man


def test_to_str():
    hang = Hang_man()
    lst = ['a', 'b', 'c']
    result = hang.to_str(lst)
    assert result == 'abc'
