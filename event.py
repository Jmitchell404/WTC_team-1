# Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/calendar/quickstart/python
# Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# stored credentials.
import cred_handler
from googleapiclient.discovery import build

creds = cred_handler.cred_valid()
service = build('calendar', 'v3', credentials=creds)

def create_event():
    event = {
    'summary': 'Google I/O 2015',
    'location': '17-85 Bromwell St, Woodstock, Cape Town, 7915',
    'description': 'A chance to hear more about Google\'s developer products.',
    'start': {
        'dateTime': '2022-02-02T09:00:00+02:00',
        'timeZone': 'Europe/London',
    },
    'end': {
        'dateTime': '2022-02-09T17:00:00+02:00',
        'timeZone': 'Europe/London',
    },
    'attendees': [
        {'email': input('put email here: ')},
    ],
    'reminders': {
        'useDefault': False,
        'overrides': [
        {'method': 'email', 'minutes': 24 * 60},
        {'method': 'popup', 'minutes': 10},
        ],
    },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))

create_event()