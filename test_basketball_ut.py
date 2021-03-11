# This unittest file tests BasketballPlayer class

import datetime
import random
import unittest
import string
from Basketball_players import BasketballPlayer, NameTooLong, \
    IllegalName, IllegalHeight, LastNameTooLong, IllegalLastName


class TestBasketballPlayer(unittest.TestCase):

    def test_long_name(self):
        """The test check if the length of the name less than 50 symbols"""
        expected_name = "James" * 11
        expected_last_name = "Harden"
        expected_birth_year = 1989
        expected_height = 196
        with self.assertRaises(expected_exception=NameTooLong):
            obj = BasketballPlayer(name=expected_name,
                                   last_name=expected_last_name,
                                   birth_year=expected_birth_year,
                                   height=expected_height)

    def test_illegal_chars_in_name(self):
        """The test check if the name does not contain illegal characters"""
        illegal_chars = string.digits + string.punctuation + string.whitespace
        for illegal_char in illegal_chars:
            shuffled_name = [illegal_char + "James"]
            random.shuffle(shuffled_name)
            for expected_name in [illegal_char + "James",
                                  "Jam" + illegal_char + "es",
                                  "James" + illegal_char]:
                expected_last_name = "Harden"
                expected_birth_year = 1989
                expected_height = 196
                with self.assertRaises(expected_exception=IllegalName):
                    obj = BasketballPlayer(name=expected_name,
                                           last_name=expected_last_name,
                                           birth_year=expected_birth_year,
                                           height=expected_height)

    def test_long_last_name(self):
        """The test check if the length of the last name less than 50 symbols"""
        expected_name = "James"
        expected_last_name = "Harden"*11
        expected_birth_year = 1989
        expected_height = 196
        with self.assertRaises(expected_exception=LastNameTooLong):
            obj = BasketballPlayer(name=expected_name,
                                   last_name=expected_last_name,
                                   birth_year=expected_birth_year,
                                   height=expected_height)

    def test_illegal_chars_in_last_name(self):
        """The test check if the last name does not contain illegal characters"""
        illegal_chars = string.digits + string.punctuation + string.whitespace
        for illegal_char in illegal_chars:
            shuffled_last_name = [illegal_char + "Harden"]
            random.shuffle(shuffled_last_name)
            for expected_last_name in [illegal_char + "Harden",
                                  "Har" + illegal_char + "den",
                                  "Harden" + illegal_char]:
                expected_name = "James"
                expected_birth_year = 1989
                expected_height = 196
                with self.assertRaises(expected_exception=IllegalLastName):
                    obj = BasketballPlayer(name=expected_name,
                                           last_name=expected_last_name,
                                           birth_year=expected_birth_year,
                                           height=expected_height)

    def test_age(self):
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

        self.assertEqual(obj.age, expected_age)

    def test_height(self):
        """The test check if the height does not contain illegal characters"""
        expected_name = "James"
        expected_last_name = "Harden"
        expected_birth_year = 1989
        expected_height = "abc"
        with self.assertRaises(expected_exception=IllegalHeight):
            obj = BasketballPlayer(name=expected_name,
                                   last_name=expected_last_name,
                                   birth_year=expected_birth_year,
                                   height=expected_height)


if __name__ == '__main__':
    unittest.main()
