import builtins

import mock
import pytest

from ..hangman.hangman import Player


def test_get_letter_right_format():
    p = Player()
    letter = 'a'
    with mock.patch.object(builtins, 'input', lambda _: letter):
        result = p.get_letter()
        assert letter == result


def test_get_letter_cap_letter():
    p = Player()
    letter = 'A'
    with mock.patch.object(builtins, 'input', lambda _: letter):
        result = p.get_letter()
        assert letter.lower() == result


def test_get_letter_dig():
    p = Player()
    letter = '1'
    with mock.patch.object(builtins, 'input', lambda _: letter):
        result = p.get_letter()
        assert result is False


def test_get_letter_seq():
    p = Player()
    letter = 'iugkb56'
    with mock.patch.object(builtins, 'input', lambda _: letter):
        result = p.get_letter()
        assert result is False
