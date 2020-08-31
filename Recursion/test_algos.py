import unittest
import super_algos
import sys
import io


class TestFunctions(unittest.TestCase):

    def test_find_min(self):
        sys.stdout = io.StringIO()
        self.assertEqual(super_algos.find_min([4,6,7,3,4,5,7]), 3)
        self.assertEqual(super_algos.find_min(["a",1,2,3,4,5]), -1)
        self.assertEqual(super_algos.find_min([6,6,1,3,5,6,1,"b"]), -1)
        self.assertEqual(super_algos.find_min([]), -1)
        self.assertEqual(super_algos.find_min([9,7,3,6,2,7,1,1,1,1,1,1]), 1)


    def test_sum_all(self):
        sys.stdout = io.StringIO()
        self.assertEqual(super_algos.sum_all([1,2,3,4,5]), 15)
        self.assertEqual(super_algos.sum_all(["a"]), -1)
        self.assertEqual(super_algos.sum_all([1,2,3,4,5,"a"]), -1)
        self.assertEqual(super_algos.sum_all([10,10,10,10,10]), 50)
        self.assertEqual(super_algos.sum_all([]), -1)
        self.assertEqual(super_algos.sum_all([25, 5, 7, 3, 9, 12]), 61)

        
if __name__ == '__main__':
    unittest.main()