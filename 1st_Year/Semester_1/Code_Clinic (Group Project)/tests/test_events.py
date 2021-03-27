import unittest
import input_validation
from io import StringIO
from test_base import captured_io
import sys


class   MyTestCase(unittest.TestCase):

    maxDiff = None
    def  test_days(self):
        with captured_io(StringIO("\n")) as (out,err):
            result = input_validation.get_days()
        output = out.getvalue().strip()
        self.assertEqual(result, 7)
        self.assertEqual(output,"""How many days would you like to display? [Leave blank for 7 days]:""")


    def  test_letter_for_day(self):
        with captured_io(StringIO("a\n10\n")) as (out,err):
            result = input_validation.get_days()
        output = out.getvalue().strip()
        self.assertEqual(output,"""How many days would you like to display? [Leave blank for 7 days]: Sorry, 'a' is not a valid argument, 'events' takes a digit as an optional parameter.
How many days would you like to display? [Leave blank for 7 days]:""")


    def  test_for_day(self):
        with captured_io(StringIO("5\n")) as (out,err):
            results = input_validation.get_days()
        output = out.getvalue().strip()
        self.assertEqual(results, 5)
        self.assertEqual(output, """How many days would you like to display? [Leave blank for 7 days]:""")


    def  test_correct_time(self):
        with captured_io(StringIO("13:30")) as (out,err):
            result = input_validation.get_time()
        output = out.getvalue().strip()
        self.assertEqual(result, ['13','30'])
        self.assertEqual(output, """Please enter the time (hh:mm):""")


    def  test_two_pm_in_time(self):
        with captured_io(StringIO("14:30")) as (out,err):
            result = input_validation.get_time()
        output = out.getvalue().strip()
        self.assertEqual(result,['14','30'])
        self.assertEqual(output, """Please enter the time (hh:mm):""")


    def test_date(self):
        with captured_io(StringIO("03/10")) as (out,err):
            result = input_validation.get_date()
        output = out.getvalue().strip()
        self.assertEqual(result,['03','10'])
        self.assertEqual(output, """Please enter the date (dd/mm):""")


    def test_jan_date(self):
        with captured_io(StringIO("04/01"))as(out,err):
            result = input_validation.get_date()
        output = out.getvalue().strip()
        self.assertEqual(result,["04","01"])
        self.assertEqual(output, """Please enter the date (dd/mm):""")


if __name__ == '__main__':
    unittest.main()
    
# # with captured_io(StringIO('HAL\nmazerun right\noff\n')) as (out, err):
# # output = out.getvalue().strip()