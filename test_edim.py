import unittest
from edim import *

class TestEdim(unittest.TestCase):
    def test_color(self):
        newColor = "red"
        path = "./test_image/lena.png"

        color(newColor, path)

if __name__ == "__main__":
    unittest.main()

