import pickle

class Roster:
    def __init__(self, shifts, people):
        self.people = people
        self.shifts = shifts
        self.start_date = None
        self.end_date = None

    def __str__(self):
        people = ', '.join(self.people)
        shifts = '------------\n'.join(list(map(str, self.shifts)))

        info_str = "People: {people}\nShifts: {shifts}\nStart Date: {start_date}\nEnd Date: {end_date}".format(
            people=people,
            shifts=shifts,
            start_date=self.start_date,
            end_date=self.end_date
        )

        return info_str

    def __repr__(self):
        people = ', '.join(self.people)
        shifts = ', '.join(list(map(repr, self.shifts)))

        info_str = "Roster(people={people}, shifts={shifts}, start_date={start_date}, end_date={end_date})".format(
            people=people,
            shifts=shifts,
            start_date=self.start_date,
            end_date=self.end_date
        )

        return info_str

    def save(self):
        pickle.dump(self, open('saves/roster.p', 'wb'))

    @staticmethod
    def load(file_name):
        return pickle.load(open('saves/roster.p', 'rb'))
