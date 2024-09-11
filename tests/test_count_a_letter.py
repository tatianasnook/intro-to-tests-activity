from main import count_a_letter
import pytest

def test_demo_one():
    num_1 = 8
    num_2 = 9

    result = num_1 + num_2

    assert result == 17

def test_demo_two():
    num_1 = 18
    num_2 = 24

    result = num_1 + num_2

    assert result == 42
# Delete the demo tests and add your tests here 