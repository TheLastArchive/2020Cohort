import unittest
from unittest.mock import patch
import io 
from io import StringIO
import sys
import mastermind

class TestFunctions(unittest.TestCase):

    def test_create_code(self):

        x = 0
        while(x < 100):
            self.assertEqual(len(set(mastermind.create_code())), 4)
            x += 1


    def test_check_correctness(self):
        sys.stdout = io.StringIO()
        self.assertTrue(mastermind.check_correctness(7, 4))
        self.assertFalse(mastermind.check_correctness(7, 3))


    @patch("sys.stdin", StringIO("1\n12\n123\n1234"))
    def test_get_answer_input(self):
        self.assertEqual(len(mastermind.get_answer_input()), 4)


    @patch("sys.stdin", StringIO("4321\n1423\n1243\n1235\n5678\n1234"))
    def test_take_turn(self):
        code = [1,2,3,4]
        self.assertEqual(mastermind.take_turn(code), 0, 4)
        self.assertEqual(mastermind.take_turn(code), 1, 3)
        self.assertEqual(mastermind.take_turn(code), 2, 2)
        self.assertEqual(mastermind.take_turn(code), 3, 0)
        self.assertEqual(mastermind.take_turn(code), 0, 0)
        self.assertEqual(mastermind.take_turn(code), 4, 0)


if __name__ == '__main__':
    unittest.main() 

    """Adding a main allows for the test to be called with
        'python3 test_functions.py'. efishinsea"""