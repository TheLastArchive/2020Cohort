import robot
import unittest
import io
import sys

class TestFunction(unittest.TestCase):

    def test_help_command(self):
        sys.stdout = io.StringIO()
        robot_data = {'name': "", 'x': 0, 'y': 0, 'compass': [1, 2, -1, -2], 'power': True, 'movements': []}

        self.assertEqual(robot.help_command(robot_data, 3), robot_data)


    def test_save_command(self):

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