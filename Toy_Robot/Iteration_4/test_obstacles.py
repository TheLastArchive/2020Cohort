from world import obstacles
import unittest
import io
import sys

class TestFunction(unittest.TestCase):

    def test_is_position_blocked(self):
        #the_obstacles = [(-43, 134, -39, 138), (-1, 105, 3, 109), (-7, -82, -3, -78), (77, -88, 81, -84)]

        self.assertFalse(obstacles.is_position_blocked(-41, 136))
        self.assertFalse(obstacles.is_position_blocked(-9, -82))
        self.assertFalse(obstacles.is_position_blocked(-41, 139))
        self.assertFalse(obstacles.is_position_blocked(-50, 137))


if __name__ == '__main__':
    unittest.main()
