#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
#
### Imports ################################

import unittest

from name2gender import get_gender


### name2gender Tests ######################

class TestGetGender(unittest.TestCase):

### Assert Functions #######################

    def composeAssert(gender):
        def func(self, name):
            name_gender = get_gender(name)
            self.assertEqual(name_gender, gender)

        return func

    assertMale = composeAssert("male")
    assertFemale = composeAssert("female")
    assertNoneGender = composeAssert(None)

### Tests ##################################

    def test_male(self):
        self.assertMale("Michal")
        self.assertMale("Tomáš")

    def test_female(self):
        self.assertFemale("Petra")
        self.assertFemale("Adéla")

    def test_last_name(self):
        self.assertFemale("Robin Svratecká")
        self.assertMale("Robin Svratecký")

    def test_unknown(self):
        self.assertNoneGender("velký rýč")
        self.assertNoneGender("Lukas Gregor")

    def test_low_case(self):
        self.assertFemale("pavlína")
        self.assertMale("lukáš")


### Main ###################################

if __name__ == "__main__":
    unittest.main()
