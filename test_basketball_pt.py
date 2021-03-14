import datetime

import pytest
from Basketball_players import BasketballPlayer, NameTooLong, \
    IllegalName, IllegalHeight, LastNameTooLong, IllegalLastName


def test_raises_exception_on_non_string_arguments():
    with pytest.raises(expected_exception=TypeError):
        "semaphore".capitalize(9)


def test_basic():
    expected_name = "James"
    expected_last_name = "Harden"
    expected_birth_year = 1989
    expected_height = 196
    player = BasketballPlayer(name=expected_name,
                              last_name=expected_last_name,
                              birth_year=expected_birth_year,
                              height=expected_height)
    assert player.name == expected_name
    assert player.last_name == expected_last_name
    assert player.birth_year == expected_birth_year
    assert player.height == expected_height


def test_long_name():
    """The test check if the length of the name less than 50 symbols"""
    expected_name = "James"
    expected_last_name = "Harden"
    expected_birth_year = 1989
    expected_height = 196
    with pytest.raises(expected_exception=NameTooLong):
        BasketballPlayer(name=expected_name,
                         last_name=expected_last_name,
                         birth_year=expected_birth_year,
                         height=expected_height)


def test_illegal_chars_in_name():
    """The test check if the name does not contain illegal characters"""
    expected_name = "James"
    expected_last_name = "Harden"
    expected_birth_year = 1989
    expected_height = 196
    with pytest.raises(expected_exception=IllegalName):
        BasketballPlayer(name=expected_name,
                         last_name=expected_last_name,
                         birth_year=expected_birth_year,
                         height=expected_height)


def test_long_last_name():
    """The test check if the length of the last name less than 50 symbols"""
    expected_name = "James"
    expected_last_name = "Harden" * 11
    expected_birth_year = 1989
    expected_height = 196
    with pytest.raises(expected_exception=LastNameTooLong):
        BasketballPlayer(name=expected_name,
                         last_name=expected_last_name,
                         birth_year=expected_birth_year,
                         height=expected_height)


def test_illegal_chars_in_last_name():
    """The test check if the last name does not contain illegal characters"""
    expected_name = "James"
    expected_last_name = "Harden!23"
    expected_birth_year = 1989
    expected_height = 196
    with pytest.raises(expected_exception=IllegalLastName):
        BasketballPlayer(name=expected_name,
                         last_name=expected_last_name,
                         birth_year=expected_birth_year,
                         height=expected_height)


def test_age():
    """The test check if the age is correct"""
    date_now = datetime.datetime.now().year
    expected_name = "James"
    expected_last_name = "Harden"
    expected_birth_year = 1989
    expected_height = 196
    expected_age = date_now - expected_birth_year
    obj = BasketballPlayer(name=expected_name,
                           last_name=expected_last_name,
                           birth_year=expected_birth_year,
                           height=expected_height)
    assert obj.age == expected_age


def test_height():
    """The test check if the height does not contain illigal digits"""
    expected_name = "James"
    expected_last_name = "Harden"
    expected_birth_year = 1989
    expected_height = '196'+'abc'
    with pytest.raises(expected_exception=IllegalHeight):
        BasketballPlayer(name=expected_name,
                         last_name=expected_last_name,
                         birth_year=expected_birth_year,
                         height=expected_height)
