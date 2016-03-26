from lib.uploader.base_uploader import BaseUploader
from .event import Event


import argparse
import httplib2
import time
import sys
import os

from apiclient.discovery import build
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import OAuth2WebServerFlow

import traceback

API_SCOPE = 'https://www.googleapis.com/auth/calendar'


class GoogleCalendarUploader(BaseUploader):
    def __init__(self, roster, client_id=None, client_secret=None):
        super(GoogleCalendarUploader, self).__init__(roster)

        self._set_credentials(client_id, client_secret)
        self.service = self._make_service()

    def _make_service(self):
        flow = OAuth2WebServerFlow(self.client_id, self.client_secret, API_SCOPE)

        storage = Storage('credentials.dat')
        credentials = storage.get()

        if credentials is None or credentials.invalid:
            flags = tools.argparser.parse_args(args=['--noauth_local_webserver'])
            credentials = tools.run_flow(flow, storage, flags)

        http = httplib2.Http()
        http = credentials.authorize(http)

        return build('calendar', 'v3', http=http)

    def _set_credentials(self, client_id, client_secret):
        if not client_id:
            client_id = os.environ.get('GCAL_CLIENT_ID')

        if not client_secret:
            client_secret = os.environ.get('GCAL_CLIENT_SECRET')

        missing = []
        for env_var in ['GCAL_CLIENT_ID', 'GCAL_CLIENT_SECRET']:
           if not os.environ.get('GCAL_CLIENT_ID'):
               missing.append(env_var)

        if len(missing) > 0:
            raise Exception('Missing Google API credentials. [{}]'.format(', '.join(missing)))

        self.client_id = client_id
        self.client_secret = client_secret


    def _upload_shift(self, shift):
        event, calendar_id = Event(shift, test=True).export()
        print(event, calendar_id)
        resp = self.service.events().insert(body=event, calendarId=calendar_id).execute()
        time.sleep(1)


    def upload_roster(self):
        try:
            shifts = self.roster.shifts
            for shift in shifts:
                self._upload_shift(shift)
        except Exception as e:
            print('Roster upload failed. Saving progress. Error: {}'.format(e))
            print(traceback.format_exc())
            self.roster.save()

