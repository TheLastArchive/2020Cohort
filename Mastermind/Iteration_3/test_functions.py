import unittest
import io 
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


if __name__ == '__main__':
    unittest.main()