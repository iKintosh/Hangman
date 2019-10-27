import builtins

import mock

from ..hangman.hangman import Player


def test_get_letter_right_format():
    play = Player()
    letter = 'a'
    with mock.patch.object(builtins, 'input', lambda _: letter):
        result = play.get_letter()
        assert letter == result


def test_get_letter_cap_letter():
    play = Player()
    letter = 'A'
    with mock.patch.object(builtins, 'input', lambda _: letter):
        result = play.get_letter()
        assert letter.lower() == result


def test_get_letter_dig():
    play = Player()
    letter = '1'
    with mock.patch.object(builtins, 'input', lambda _: letter):
        result = play.get_letter()
        assert result is False


def test_get_letter_seq():
    play = Player()
    letter = 'iugkb56'
    with mock.patch.object(builtins, 'input', lambda _: letter):
        result = play.get_letter()
        assert result is False
