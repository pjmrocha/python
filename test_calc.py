import calc
import unittest

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1,2) == 3, "It should be 3")
        print("Test Ok") 

