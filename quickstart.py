"""
Shows basic usage of the Google Calendar API. Creates a Google Calendar API
service object and outputs a list of the next 10 events on the user's calendar.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime

# Setup the Calendar API
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
store = file.Storage('/path/to/your/credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('/path/to/your/client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))

# Call the Calendar API
now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
twowahead = (datetime.datetime.utcnow() + datetime.timedelta(weeks=2)).isoformat() + 'Z'
# Fetching up to 50 events from the next 2 weeks
events_result = service.events().list(calendarId='primary', timeMin=now,
                                      maxResults=50, singleEvents=True,
                                      orderBy='startTime',
                                      timeMax=twowahead).execute()
events = events_result.get('items', [])

if not events:
    raise ValueError('Failed to fetch events.')
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    print([start, event['summary']])