
class Roster:
	def __init__(self):
		self.people = []
		self.shifts = []
		self.start_date = None
		self.end_date = None


	def __str__(self):
		people = ','.join(self.people)
		shifts = ','.join(self.shift)
		
		info_str = \
		"""
		People: {people}
		Shifts: {shifts}
		Start Date: {start_date}
		End Date: {end_date}
		""".format(people, shifts, self.start_date, self.end_date)

		return info_str


	def add_shift(shift):
		pass


	def add_person(person):
		pass

	

