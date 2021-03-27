import unittest
from io import StringIO
import os
import events
import datetime
import json

CALENDAR_ID = None #Your calendar ID here
events.username = None #Your username for testing purposes here

# self.assertTrue(output.find('starting maze run..') > -1)

class   MyTestCase(unittest.TestCase):
    maxDiff = None
    def test_clinic(self):
        with os.popen("./clinic\n") as clinic:
            clinic_output = clinic.read()
            clinic.close()
        self.assertEqual(clinic_output,"""
clinic <command> <paramters>
List of all clinic commands:

    events        Retrieves and lists all the events from the calendar for the 
given days.

                  Parameters: Days(digit)  >  Set how many days worth of events 
to search for 
                              'personal'   >  Display your personal calendar's 
events

    volunteer     Creates an event on the calendar.

                  Parameters: Date         > The date for the event
                              Time         > The start time for the event
                              Summary      > The name of the event, keep it 
concise 

    book          Add yourself to a pre-existing event.

                  Parameters: Event ID     > ID for the event you'd like to 
attend

    cancel        Remove yourself from an event, the event will be deleted if 
the volunteer cancels.

                  Parameters: Event ID     > ID for the event you'd like to 
attend

    my_events     Lists all the events you have created/subscribed to

        
Parameters are not mandatory, simply call the command for a walkthrough on the 
necessary information.

""")


if __name__ == '__main__':
    unittest.main()
    