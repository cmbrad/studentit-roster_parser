import pytz

CALENDARS = {
    '': ''
}

TEST_CALENDARS = {
    'Baillieu': 'testBaillieu',
    #'Baillieu': '1j2orr1n9hknge9lhvk5420thg@group.calendar.google.com',
    'BEE': 'pve28up8ppbineq2a4uq30ht8c@group.calendar.google.com',
    'Giblin Eunson': 'pve28up8ppbineq2a4uq30ht8c@group.calendar.google.com',
    'ERC': '07n1c1aii2dmhu5cn137im3tcc@group.calendar.google.com'
}

TIMEZONE = pytz.timezone("Australia/Melbourne")


class Event(object):
    def __init__(self, shift, test=False):
        self.calendars = CALENDARS if not test else TEST_CALENDARS
        self.body = self._make_body(shift)

        self.calendar_id = self._loc_to_calendar(shift.location)

    def export(self):
        return self.body, self.calendar_id

    def _loc_to_calendar(self, location):
        return self.calendars[location]

    def _make_body(self, shift):
        return {
            'summary': shift.person,
            'location': shift.location,
            'start': {
                'dateTime': shift.start_time.isoformat(),
                'timeZone': str(TIMEZONE),
            },
            'end': {
                'dateTime': shift.end_time.isoformat(),
                'timeZone': str(TIMEZONE),
            },
            'attendees': [
                {
                    'email': '',
                    'displayName': '',
                    'ResponseStatus': 'accepted'
                }
            ],
            'organizer': {
                'email': '',
                'displayName': ''
            },
            'guestsCanModify': True
        }

