import datetime
import pickle
import os
from save_client_info import *
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pprint import pprint
import pathlib

SCOPES = ['https://www.googleapis.com/auth/calendar']
PATH = str(pathlib.Path.home()) + "/bin/clinic/"

def  auth_check():
    username = input("Username: ")
    email = input("Email: ")
    if username in email and "student" in email and "wethinkcode" in email:
        print("Hello fellow student how can I assist you?")
        save_info(username, email)
        return True
    elif username in email and "wethinkcode" in email:
        print("welcome, "+username+", we've been expecting you")
        return True
        
    else:
        print("Incorrect email/username. please enter valid WeThinkCode username/email")
        return False


def  main():
    
    new_credentials = None

    if os.path.exists(PATH + "tokens/token.pickle"):
        with open(PATH + "tokens/token.pickle", "rb") as token:
            new_credentials = pickle.load(token)
    if not new_credentials or not new_credentials.valid:
        if new_credentials and new_credentials.expired and new_credentials.refresh_token:
            print("Updating calendar data")
            new_credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                PATH + 'credentials.json',SCOPES)
            new_credentials = flow.run_local_server(port=0)
            auth_check()
        with open(PATH + "tokens/token.pickle","wb") as token:
            pickle.dump(new_credentials,token)
    service = build('calendar','v3', credentials=new_credentials)
    remove_user_events()

    return service


def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    """Source code from Jie Jinn - https://learndataanalysis.org/google-py-file-source-code/
    Takes input and converts it to the RFC format for easier use."""

    return datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
