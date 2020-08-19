import unittest

from est import (
	h, Hour,
	d, Day,
)


class Test_Hour(unittest.TestCase):

	#
	# init
	#
	def test_init_int(self):
		want = 2

		got = Hour(2).val

		self.assertEqual(want, got)

	def test_init_h(self):
		want = 2

		got = Hour(2*h).val

		self.assertEqual(want, got)

	#
	# eq
	#
	def test_eq_True(self):
		want = True

		got = (2*h == 2*h)

		self.assertEqual(want, got)
	
	def test_eq_False(self):
		want = False

		got = (2*h == 3*h)

		self.assertEqual(want, got)

	#
	# str
	#
	def test_str(self):
		want = "1h"

		got = str(1*h)

		self.assertEqual(want, got)

	#
	# mul
	#
	def test_const_rmul(self):
		want = "6h"

		got = str(2*3*h)

		self.assertEqual(want, got)

	def test_const_mul(self):
		want = "6h"

		got = str(h*3*2)

		self.assertEqual(want, got)

	def test_const_rmul_mul(self):
		want = "6h"

		got = str(3*h*2)

		self.assertEqual(want, got)

	def test_hour_mul(self):
		want = "2h"

		got = str(2*h*1*h)

		self.assertEqual(want, got)


class Test_Day(unittest.TestCase):

	#
	# init
	#
	def test_init_int(self):
		want = 2

		got = Day(2).val

		self.assertEqual(want, got)

	def test_init_h(self):
		want = 2

		got = Day(2*d).val

		self.assertEqual(want, got)

	#
	# eq
	#
	def test_eq_True(self):
		want = True

		got = (2*d == 2*d)

		self.assertEqual(want, got)
	
	def test_eq_False(self):
		want = False

		got = (2*d == 3*h)

		self.assertEqual(want, got)

	#
	# str
	#
	def test_str(self):
		want = "1d"

		got = str(1*d)

		self.assertEqual(want, got)

	#
	# mul
	#
	def test_const_rmul(self):
		want = "6d"

		got = str(2*3*d)

		self.assertEqual(want, got)

	def test_const_mul(self):
		want = "6d"

		got = str(d*3*2)

		self.assertEqual(want, got)

	def test_const_rmul_mul(self):
		want = "6d"

		got = str(3*d*2)

		self.assertEqual(want, got)

	def test_day_mul(self):
		want = "2d"

		got = str(2*d*1*d)

		self.assertEqual(want, got)


class Test_Hour_Day(unittest.TestCase):

	#
	# init
	#
	def test_str(self):
		want = ""

		got = str(2*d*1*h)

		self.assertEqual(want, got)


if __name__ == "__main__":
	unittest.main()
