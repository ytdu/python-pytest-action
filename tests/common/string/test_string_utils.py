import pytest

from app.common.string import string_utils


def test_to_caps():
    s = 'new york'
    assert string_utils.to_caps(s) == 'New York'
    s = 'tri-valley'
    assert string_utils.to_caps(s) == 'Tri-Valley'
    s = 'some -- x '
    assert string_utils.to_caps(s) == 'Some -- X '


def test_is_whole_word():
    s = 'san francisco'
    assert string_utils.is_whole_word(s, 0, 3)
    assert not string_utils.is_whole_word(s, 0, 4)


def test_str2bool():
    assert string_utils.str2bool('1')
    assert string_utils.str2bool('t')
    assert string_utils.str2bool('True')
    assert not string_utils.str2bool('0')
    assert not string_utils.str2bool('N')
    assert not string_utils.str2bool('false')
    with pytest.raises(ValueError):
        string_utils.str2bool('unknown')
