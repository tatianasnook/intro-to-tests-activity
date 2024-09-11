from main import count_a_letter
import pytest

def test_count_a_letter():
    sentence = 'Hello World!'
    letter = 'l'

    result = count_a_letter(sentence, letter)
    assert result == 3


def test_count_a_letter_check_letter_is_valid():
    sentence = 'Hello World!'
    letter = '2'

    result = count_a_letter(sentence, letter)
    assert result == None


def test_count_a_letter_check_sentence_is_empty():
    sentence = ''
    letter = 'e'

    result = count_a_letter(sentence, letter)
    assert result == None


def test_count_a_letter_check_sentence_is_valid():
    sentence = '12345'
    letter = 'l'

    result = count_a_letter(sentence, letter)
    assert result == None
