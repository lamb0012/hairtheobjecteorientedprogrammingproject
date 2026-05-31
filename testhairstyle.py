import unittest
from hairstyle import get_hair, curly_hair, straight_hair, fluffy_hair, no_hair, toomuch_hair

class testhairstyles(unittest.testcase):

    def test_valid_curly(self):
        obj = get_hair("curly")
        self.assertIsInstance(obj, curly_hair)

    def test_valid_straight(self):
        obj = get_hair("straight")
        self.assertIsInstance(obj, straight_hair)

    def test_valid_fluffy(self):
        obj = get_hair("fluffy")
        self.assertIsInstance(obj, fluffy_hair)

    def test_invalid_input(self):
        obj = get_hair("alien")
        self.assertIsNone(obj)

if __name__ == "__main__":
    unittest.main()
