class Shift:
    def __init__(self, start_time=None, end_time=None, person=None, location=None):
        self.start_time = start_time
        self.end_time = end_time
        self.person = person
        self.location = location

    def __str__(self):
        return "Person: {person}\nLocation: {location}\nStart Time: {start_time}\nEnd Time: {end_time}\n".format(
                person=self.person,
                location=self.location,
                start_time=self.start_time,
                end_time=self.end_time)

    def __repr__(self):
        return "Shift(person={person}, location={location}, start_time={start_time}, end_time={end_time}".format(
                person=self.person,
                location=self.location,
                start_time=self.start_time,
                end_time=self.end_time)
