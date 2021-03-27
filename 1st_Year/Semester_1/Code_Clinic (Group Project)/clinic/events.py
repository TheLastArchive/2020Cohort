from quickstart import main, convert_to_RFC_datetime
import datetime
from create_table import create_table, create_table_personal
from pprint import pprint
import json
from input_validation import free_busy
from save_client_info import update_user_events, remove_user_events
import pathlib

CALENDAR_ID = None #Your Google Calendar ID here 
service = main()
PATH = str(pathlib.Path.home()) + "/bin/clinic/"

with open(PATH + "client_file.json") as f:
        user = json.load(f)
        email = user["email"]
        username = email.split("@")[0]
        user_events = user['events']

def get_events(startDate, endDate):
    """Connects to the Google Calendar API and returns all the events for the given amount of days"""

    response = service.events().list(
        calendarId=CALENDAR_ID,
        singleEvents=True,
        orderBy='startTime',
        timeMin=startDate,
        timeMax=endDate
    ).execute()

    if response['items'] == []:
        print("No clinic events found")
        return response

    handle_clinic_info(response['items'])  


def handle_clinic_info(items):
    """Goes through the jumbled mess that the API spits out and picks up the information we need"""

    # We need the event id, summary, creator, attendees and start
    for item in items:
        event_id = str(item.get('id'))
        summary = str(item.get('summary'))
        temp = item.get('creator')
        volunteer = str((temp.get('email')).split('@')[0])
        #The attendees of the event will be the students. Try Except since a key error is raised if there
        #are no attendees.
        try: 
            students = []
            for attendee in item['attendees']:
                student = str(attendee['email'].split('@')[0])
                students.append(student)
        except KeyError: pass
        #The start date and time for the event
        temp = item.get('start')
        dt = datetime.datetime.strptime(temp.get('dateTime'), '%Y-%m-%dT%H:%M:%S+02:00')
        day = dt.day
        month = dt.month
        hour = dt.hour
        mins = dt.minute

        create_table(summary=summary, students=students, day=day, month=month, hour=hour, mins=mins, volunteer=volunteer, event_id=event_id)


def get_personal_events(startDate, endDate):
    """Receives the information from the user's personal calendar"""

    response = service.events().list(
        calendarId=email,
        singleEvents=True,
        orderBy='startTime',
        timeMin=startDate,
        timeMax=endDate
    ).execute()

    if response['items'] == []:
        print("No personal events found")
        return response
    handle_personal_info(response['items'])


def handle_personal_info(items):
    """Sorts through the API response and picks the information we want"""
    
    for item in items:
        summary = str(item.get('summary'))
        temp = item.get('start')
        dt = datetime.datetime.strptime(temp.get('dateTime'), '%Y-%m-%dT%H:%M:%S+02:00')
        day = dt.day
        month = dt.month
        hour = dt.hour
        mins = dt.minute

        create_table_personal(summary=summary, day=day, month=month, hour=hour, mins=mins)


def edit_event(event_id):
    """Adds the user as an attendee for the given event"""

    print("Fetching event...")
    response = service.events().get(calendarId=CALENDAR_ID, eventId=event_id).execute()

    startTime = response['start']
    startTime = startTime['dateTime']
    endTime = response['end']
    endTime = endTime['dateTime']
    if free_busy(startTime, endTime, book=True) is False: return
        
    #Try except loop since a key error is raised if there are no attendees
    if len(response['attendees']) > 3:
        print("Sorry, this event is fully booked")
        return
    print("Booking slot...")
    response['attendees'].append({'email': email})
    
    update_user_events(endTime, response.get('id'))
    
    response = service.events().update(
        calendarId=CALENDAR_ID,
        eventId=event_id,
        body=response,
        sendNotifications=True,
        sendUpdates='all'
    ).execute()
    print("Slot booked")
    
    return response


def create_event(start, end, summary):
    """Creates a Google Calendar event"""

    event_body = {
        'start': {
            'dateTime': start,
            'timeZone': 'Africa/Johannesburg'
        },
        'end': {
            'dateTime': end,
            'timeZone': 'Africa/Johannesburg'
        },
        'summary': str(summary),
        'attendees': [{
            'email': email,
            'creator': True
            }]
        }

    response = service.events().insert(
        calendarId=CALENDAR_ID,
        maxAttendees=4,
        sendNotifications=True,
        body=event_body).execute()
    print("Slot created")
    print(f"Your event ID is {response.get('id')}")
    update_user_events(response['end']['dateTime'], response.get('id'))

    return response


def cancel_event(event_id):
    """Either deletes an event if user is the volunteer (event creator)
    and there are no attendees, or removes the user if they are a student"""

    #Gets the event object from the API
    print("Fetching event...")
    response = service.events().get(
        calendarId=CALENDAR_ID,
        eventId=event_id).execute()
    #Checks if the event has only one attendee (the event creator)
    if len(response['attendees']) == 1:
        #If user is the event creator, delete the event
        if response['creator']['email'] == email:
            print("Event deleted")
            remove_user_events(event_id=event_id)
            return service.events().delete(
                calendarId=CALENDAR_ID, 
                eventId=event_id,
                sendNotifications=True,
                sendUpdates="all").execute()
        else:
            print("You can not cancel another student's event.")
    #If user is not the event creator, check if they are an attendee
    elif response['creator']['email'] != email:
        attendees = response['attendees']
        for i in range(0, len(attendees)):
            if attendees[i]['email'] == email:
                attendees.pop(i)
                response['attendees'] = attendees
                print("Slot cancelled")
                remove_user_events(event_id=event_id)
                return service.events().update(
                    calendarId=CALENDAR_ID, 
                    eventId=event_id,
                    body=response,
                    sendNotifications=True,
                    sendUpdates="all").execute()
        print("You are not booked for this event")

    else: print("Sorry, a student has booked for your event")


def get_user_events():

    print("Fetching events...")
    if not user_events:
        print("You have no events")
        return
    for event in user_events:
        response = service.events().get(calendarId=CALENDAR_ID,
                                        eventId=user_events[event]).execute()
        handle_clinic_info([response])

