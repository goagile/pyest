"""
1d4h    
1*d+4*h
d(1)*h(4)

h * '1d4h'

'1d4h' * h

P('1d4h') * h


"""

class Period:

	def __init__(self, weeks, days, hours):
		self.weeks = weeks
		self.days = days
		self.hours = hours

	def __str__(self):
		return "p"


class Hour:

	def __init__(self, other):

		if type(other) == type(self):
			self.val = other.val
			return

		self.val = other

	def __str__(self):
		return "{0}h".format(self.val)

	def __mul__(self, other):
		print("HOUR MUL", self, other)
		if type(other) == type(self):
			return Hour(self.val * other.val)
		return Hour(self.val * other)

	def __rmul__(self, other):
		print("HOUR R MUL", self, other)
		return self.__mul__(other)

	def __eq__(self, other):
		if type(other) != type(self):
			return False
		return (other.val == self.val)


class Day:

	def __init__(self, other):

		if type(other) == type(self):
			self.val = other.val
			return

		self.val = other

	def __str__(self):
		return "{0}d".format(self.val)

	def __mul__(self, other):
		print("DAY MUL", self, other)
		if type(other) == type(self):
			return Day(self.val * other.val)
		return Day(self.val * other)

	def __rmul__(self, other):
		print("DAY R MUL", self, other)
		if type(other) == type(self):
			return Day(self.val * other.val)
		return Day(self.val * other)

	def __eq__(self, other):
		if type(other) != type(self):
			return False
		return (other.val == self.val)


h = Hour(1)
d = Day(1)
