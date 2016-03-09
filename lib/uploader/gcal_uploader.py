from .base_uploader import BaseUploader


class GoogleCalendarUploader(BaseUploader):
    def upload_shift(self):
        pass

    def upload_roster(self):
        print(self.roster)
        shifts = self.roster.shifts
        for shift in shifts:
            print(shift)

