class Roster:
    def __init__(self, people):
        self.people = people
        self.shifts = []
        self.start_date = None
        self.end_date = None

    def __str__(self):
        people = ', '.join(self.people)
        shifts = ', '.join(self.shifts)

        info_str = "People: {people}\nShifts: {shifts}\nStart Date: {start_date}\nEnd Date: {end_date}" \
            .format(people=people,
                    shifts=shifts,
                    start_date=self.start_date,
                    end_date=self.end_date)

        return info_str

    def add_shift(self, shift):
        self.shifts.append(shift)

    def add_person(self, person):
        self.people.append(person)