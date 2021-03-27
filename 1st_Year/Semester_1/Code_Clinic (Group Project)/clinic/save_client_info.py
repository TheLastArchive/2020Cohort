import json
import datetime
import pathlib

PATH = str(pathlib.Path.home()) + "/bin/clinic/"

def save_info(user, email):
    """Creates a json file and stores the user's information"""

    user_dict = {"email" : email, 'events': {}}
    file = json.dumps(user_dict)
    f = open(PATH + "client_file.json", "w")
    f.write(file)
    f.close()


def update_user_events(endTime, event_id):
    """Adds event IDs to the user's client file""" 

    with open(PATH + "client_file.json", "r") as f:
        user_dict = json.load(f)
    #Save the key for the event as the endtime so it can be removed once the time passes
    user_dict['events'][str(endTime)] = event_id
    file = json.dumps(user_dict)

    with open(PATH + "client_file.json", "w") as f:
        f.write(file)
    

def remove_user_events(event_id=None):
    """Removes any events from the user's event list that
    are either specified as a paramter, or once the event has 
    passed it's end time."""

    with open(PATH + "client_file.json", "r") as f:
        user_dict = json.load(f)
    #If there is an event ID passed, remove that specific event first
    events = user_dict['events']
    for event in list(events):
        if events[event] == event_id:
            user_dict['events'].pop(event)
        #Checks which events have expired.
        elif datetime.datetime.strptime(event, '%Y-%m-%dT%H:%M:%S+02:00') < datetime.datetime.now():
            user_dict['events'].pop(event)

    with open(PATH + "client_file.json", "w") as f:
        file = json.dumps(user_dict)
        f.write(file)

