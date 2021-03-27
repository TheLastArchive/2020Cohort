from datetime import datetime
from quickstart import main
import json
import pathlib

service = main()
CALENDAR_ID = None #Your calendar ID here
date_format = "%d/%m"
time_format = "%H:%M"
PATH = str(pathlib.Path.home()) + "/bin/clinic/"

with open(PATH + "client_file.json") as f:
    user = json.load(f)
    email = user["email"]
    username = email.split('@')


def free_busy(start_date, end_date, book=None):
    """Uses the Google Calendar FreeBusy function to check for any event clashes"""
    requestbody = {
  "timeMin": start_date,
  "timeMax": end_date,
  "timeZone": 'Africa/Johannesburg',
  "calendarExpansionMax": 10,
  "items": [
    {
        "id": email
    },
    {
        "id": CALENDAR_ID
    }
  ]
}
    response = service.freebusy().query(body = requestbody).execute()
    return test_freebusy(response, book)
    

def test_freebusy(response, book):
    """Checks the FreeBusy response to check if there are any schedule conflicts"""

    calendars = response.get('calendars')
    for key in calendars.keys():
        if book is True and key == CALENDAR_ID: 
            continue
        calendar = calendars.get(key)
        temp = calendar['busy']
        if len(temp) > 0:
            print("You already have an event scheduled for that time")
            return False
    
    return True



def get_days():
    """Gets user input if no argument is passed for clinic events"""
    
    while True:
        days = input("How many days would you like to display? [Leave blank for 7 days]: ")
        if days == "":
            days = 7
            return days
        try:
            days = int(days)
            return days
        except:
            print(f"Sorry, '{days}' is not a valid argument, 'events' takes a digit as an optional parameter.")    


def get_date(input_date=None):
    """Gets user input if no date argument is passed for clinic volunteer, or validates
    if date argument is passed"""

    if input_date is not None:
        try:
            datetime.strptime(input_date, date_format)
            return input_date.split('/')
        except ValueError:
            print(f"sorry,{input_date} is not the correct format please use (dd/mm) format.")

    while True:
        date = input("Please enter the date (dd/mm): ")
        try:
            datetime.strptime(date, date_format)
            return date.split('/')
        except ValueError:
            print(f"sorry,{date} is not the correct format please use (dd/mm) format.")


def get_time(time=None):
    """Gets user input if no time argument is passed for clinic volunteer, or validates
    if time argument is passed"""
    
    if time is not None:
        try:
            datetime.strptime(time, time_format)
            return time.split(':')
        except ValueError:
            print(f"sorry,{time} is not the correct format please use (hh:mm) format.")    
    
    
    while True:
        time = input("Please enter the time (hh:mm): ")
        try:
            datetime.strptime(time, time_format)
            return time.split(':')
        except ValueError:
            print(f"sorry,{time} is not the correct format please use (hh:mm) format.")


