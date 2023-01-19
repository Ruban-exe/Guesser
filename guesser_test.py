import unittest
import Guesser

class MyTestCase(unittest.TestCase):
    def test_input(self):
        result = Guesser.guesser(5, 5)
        self.assertTrue(result)  # add assertion here

    def test_imput_wrong_gess(self):
        result = Guesser.guesser(5, 0)
        self.assertFalse(result)  # add assertion here

    def test_imput_wrong_number(self):
        result = Guesser.guesser(12, 3)
        self.assertIsNone(result, TypeError)  # add assertion here

    def test_imput_wrong_type(self):
        result = Guesser.guesser(5,'3')
        self.assertIsNone(result, TypeError)  # add assertion here

if __name__ == '__main__':
    unittest.main()
