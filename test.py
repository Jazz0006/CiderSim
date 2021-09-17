import unittest
from classes import Apple

class TestFruit(unittest.TestCase):
    def test_apples(self):
        apple = Apple()
        print(apple)
        self.assertIn((apple.flavour, apple.colour), [("sour", "green"), ("sweet", "red")])