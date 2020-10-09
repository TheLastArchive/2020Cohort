import unittest 
import sys
import io
from world import obstacles


class MyTestCase(unittest.TestCase):

    def test_is_position_blocked(self):

        obstacles.obstacle_list = [[0, 0, 4, 4]]

        self.assertTrue(obstacles.is_position_blocked(0, 0))
        self.assertTrue(obstacles.is_position_blocked(2, 3))

        self.assertFalse(obstacles.is_position_blocked(6, 6))
        self.assertFalse(obstacles.is_position_blocked(2, 6))


    def test_is_path_blocked(self):

        obstacles.obstacle_list = [[0, 0, 4, 4]]

        self.assertTrue(obstacles.is_path_blocked(0, 0, 0, 0))
        self.assertTrue(obstacles.is_path_blocked(0, 0, 2, 0))
        self.assertTrue(obstacles.is_path_blocked(8, 2, -4, 2))
        self.assertTrue(obstacles.is_path_blocked(0, -4, 0, 8))

        self.assertFalse(obstacles.is_path_blocked(5, -4, 5, 8))
        self.assertFalse(obstacles.is_path_blocked(0, -1, 20, -1))

    def test_get_obstacles(self):

        obstacles.obstacle_list = [[0, 0, 4, 4]]

        self.assertEqual(obstacles.get_obstacles(), obstacles.obstacle_list)
        

if __name__ == '__main__':
    unittest.main()

