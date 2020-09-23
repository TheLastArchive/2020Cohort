import robot
import unittest
import io
import sys

class TestFunction(unittest.TestCase):

    def test_help_command(self):
        sys.stdout = io.StringIO()
        robot_data = {'name': "", 'x': 0, 'y': 0, 'compass': [1, 2, -1, -2], 'power': True, 'movements': []}
        
        
        self.assertEqual(robot.help_command(robot_data, 3), robot_data)

    def test_move_forward(self):

        robot_data = {'name': "", 'x': 0, 'y': 0, 'compass': [1, 2, -1, -2], 'power': True, 'movements': []}

        self.assertEqual(robot.move_forward(robot_data, 15, 2), robot_data)
        self.assertEqual(robot.move_forward(robot_data, 10, 2), robot_data)
        self.assertEqual(robot.move_forward(robot_data, 11, 2), robot_data)
        self.assertEqual(robot.move_forward(robot_data, 20, 2), robot_data)


    def test_track_position(self):

        robot_data = {'name': "", 'x': 0, 'y': 0, 'compass': [1, 2, -1, -2], 'power': True, 'movements': []}

        self.assertEqual(robot.track_position(robot_data, 10), {'name': "", 'x': 0, 'y': 10, 'compass': [1, 2, -1, -2], 'power': True, 'movements': []})
        robot_data['y'] = 0   #It kept saving the y value between tests and this was the easiest fix
        self.assertEqual(robot.track_position(robot_data, 15), {'name': "", 'x': 0, 'y': 15, 'compass': [1, 2, -1, -2], 'power': True, 'movements': []})
        robot_data['y'] = 0
        self.assertEqual(robot.track_position(robot_data, -20), {'name': "", 'x': 0, 'y': -20, 'compass': [1, 2, -1, -2], 'power': True, 'movements': []})
        robot_data['y'] = 0
        self.assertFalse(robot.track_position(robot_data, 201))

    def test_move_back(self):

        robot_data = {'name': "", 'x': 0, 'y': 0, 'compass': [1, 2, -1, -2], 'power': True, 'movements': []}

        self.assertEqual(robot.move_back(robot_data, 10, 2), robot_data)
        self.assertEqual(robot.move_back(robot_data, 11, 2), robot_data)
        self.assertEqual(robot.move_back(robot_data, 12, 2), robot_data)
        self.assertEqual(robot.move_back(robot_data, 13, 2), robot_data)
        self.assertEqual(robot.move_back(robot_data, 14, 2), robot_data)
        self.assertEqual(robot.move_back(robot_data, 15, 2), robot_data)
    
    def test_turn(self):

        robot_data = {'name': "", 'x': 0, 'y': 0, 'compass': [1, 2, -1, -2], 'power': True, 'movements': []}

        self.assertEqual(robot.turn_left(robot_data, 2), {'name': "", 'x': 0, 'y': 0, 'compass': [-2, 1, 2, -1], 'power': True, 'movements': []})
        robot_data['compass'] = [1, 2, -1, -2]
        self.assertEqual(robot.turn_right(robot_data, 2), {'name': "", 'x': 0, 'y': 0, 'compass': [2, -1, -2, 1], 'power': True, 'movements': []})

    def test_sprint(self):

        robot_data = {'name': "", 'x': 0, 'y': 0, 'compass': [1, 2, -1, -2], 'power': True, 'movements': []}

        self.assertEqual(robot.sprint(robot_data, 5, 2), robot_data)
        self.assertEqual(robot.sprint(robot_data, 6, 2), robot_data)
        self.assertEqual(robot.sprint(robot_data, 7, 2), robot_data)
        self.assertEqual(robot.sprint(robot_data, 8, 2), robot_data)
        self.assertEqual(robot.sprint(robot_data, 9, 2), robot_data)

    def test_save_Command(self):

        robot_data = {'name': "", 'x': 0, 'y': 0, 'compass': [1, 2, -1, -2], 'power': True, 'movements': []}

        self.assertEqual(robot.save_command(robot_data, "forward 10"),\
            {'name': "", 'x': 0, 'y': 0, 'compass': [1, 2, -1, -2], 'power': True, 'movements': ["forward 10"]})
        self.assertEqual(robot.save_command(robot_data, "forward 20"),\
            {'name': "", 'x': 0, 'y': 0, 'compass': [1, 2, -1, -2], 'power': True, 'movements': ["forward 10", "forward 20"]})
        self.assertEqual(robot.save_command(robot_data, "help"),\
            {'name': "", 'x': 0, 'y': 0, 'compass': [1, 2, -1, -2], 'power': True, 'movements': ["forward 10", "forward 20"]})
        self.assertEqual(robot.save_command(robot_data, "left"),\
            {'name': "", 'x': 0, 'y': 0, 'compass': [1, 2, -1, -2], 'power': True, 'movements': ["forward 10", "forward 20", "left"]})
        self.assertEqual(robot.save_command(robot_data, "sprint 5"),\
            {'name': "", 'x': 0, 'y': 0, 'compass': [1, 2, -1, -2], 'power': True, 'movements': ["forward 10", "forward 20", "left", "sprint 5"]})


if __name__ == '__main__':
    unittest.main()