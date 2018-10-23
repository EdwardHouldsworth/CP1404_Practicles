"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    repeated_string = []
    for x in range(0, n):
        repeated_string.append(s)
    return " ".join(repeated_string)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"
    assert test_car.fuel == 0, "Car does not set fuel correctly"

    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set fuel correctly"


run_tests()

doctest.testmod()


def fix_sentence(sentence=""):
    """
    >>> fix_sentence("hello")
    'Hello.'
    >>> fix_sentence("It is an ex Parrot.")
    'It is an ex Parrot.'
    >>> fix_sentence('')
    ''
    """
    if sentence == "":
        return ""
    else:
        new_sentence = sentence[0].upper() + sentence[1:]
        if sentence[-1] == '.':
            pass
        else:
            new_sentence += '.'

    return new_sentence
