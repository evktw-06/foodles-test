from words_count import get_words_occurrences_number
import pytest


def test_get_words_occurrences_number_example():
    sentence = "baz bar foo foo zblah zblah zblah baz toto bar"
    n = 3

    result = get_words_occurrences_number(sentence, n)

    assert result == [('zblah', 3), ('bar', 2), ('baz', 2)]


def test_get_words_occurrences_number_empty_sentence():
    sentence = ""
    n = 4

    result = get_words_occurrences_number(sentence, n)

    assert result == []


def test_get_words_occurrences_number_invalid_n():
    sentence = "baz bar foo foo zblah zblah zblah baz toto bar"
    n = -3

    with pytest.raises(ValueError):
        get_words_occurrences_number(sentence, n)
