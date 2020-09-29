from world.text import world
import unittest
import io
import sys

class TestFunction(unittest.TestCase):

    def test_move_forward(self):

        robot_data = {'name': "", 'x': 0, 'y': 0, 'compass': [1, 2, -1, -2], 'power': True, 'movements': []}

        self.assertEqual(world.move_forward(robot_data, 15, 2), robot_data)
        self.assertEqual(world.move_forward(robot_data, 10, 2), robot_data)
        self.assertEqual(world.move_forward(robot_data, 11, 2), robot_data)
        self.assertEqual(world.move_forward(robot_data, 20, 2), robot_data)


    def test_track_position(self):
        sys.stdout = io.StringIO()
        robot_data = {'name': "", 'x': 0, 'y': 0, 'compass': [1, 2, -1, -2], 'power': True, 'movements': []}

        self.assertEqual(world.track_position(robot_data, 10), {'name': "", 'x': 0, 'y': 10, 'compass': [1, 2, -1, -2], 'power': True, 'movements': []})
        robot_data['y'] = 0   #It kept saving the y value between tests and this was the easiest fix
        self.assertEqual(world.track_position(robot_data, 15), {'name': "", 'x': 0, 'y': 15, 'compass': [1, 2, -1, -2], 'power': True, 'movements': []})
        robot_data['y'] = 0
        self.assertEqual(world.track_position(robot_data, -20), {'name': "", 'x': 0, 'y': -20, 'compass': [1, 2, -1, -2], 'power': True, 'movements': []})
        robot_data['y'] = 0
        self.assertFalse(world.track_position(robot_data, 201))

    def test_move_back(self):

        robot_data = {'name': "", 'x': 0, 'y': 0, 'compass': [1, 2, -1, -2], 'power': True, 'movements': []}

        self.assertEqual(world.move_back(robot_data, 10, 2), robot_data)
        self.assertEqual(world.move_back(robot_data, 11, 2), robot_data)
        self.assertEqual(world.move_back(robot_data, 12, 2), robot_data)
        self.assertEqual(world.move_back(robot_data, 13, 2), robot_data)
        self.assertEqual(world.move_back(robot_data, 14, 2), robot_data)
        self.assertEqual(world.move_back(robot_data, 15, 2), robot_data)
    
    def test_turn(self):

        robot_data = {'name': "", 'x': 0, 'y': 0, 'compass': [1, 2, -1, -2], 'power': True, 'movements': []}

        self.assertEqual(world.turn_left(robot_data, 2), {'name': "", 'x': 0, 'y': 0, 'compass': [-2, 1, 2, -1], 'power': True, 'movements': []})
        robot_data['compass'] = [1, 2, -1, -2]
        self.assertEqual(world.turn_right(robot_data, 2), {'name': "", 'x': 0, 'y': 0, 'compass': [2, -1, -2, 1], 'power': True, 'movements': []})

    def test_sprint(self):

        robot_data = {'name': "", 'x': 0, 'y': 0, 'compass': [1, 2, -1, -2], 'power': True, 'movements': []}

        self.assertEqual(world.sprint(robot_data, 5, 2), robot_data)
        self.assertEqual(world.sprint(robot_data, 6, 2), robot_data)
        self.assertEqual(world.sprint(robot_data, 7, 2), robot_data)
        self.assertEqual(world.sprint(robot_data, 8, 2), robot_data)
        self.assertEqual(world.sprint(robot_data, 9, 2), robot_data)


if __name__ == '__main__':
    unittest.main()