import unittest
from ce3_leap_year import is_leap_year

class IsLeapYearTestCase(unittest.TestCase):
	def setUp(self):
		self.is_leap_year = is_leap_year
		self.leap_years = [2000, 2004, 2008, 2012, 2016, 2020, 2024]

	def test_is_leap_year_20th_century(self):
		for i in range(self.leap_years[0], self.leap_years[-1] + 1):
			if i in self.leap_years:
				self.assertEqual(self.is_leap_year(i), True)
			else:
				self.assertEqual(self.is_leap_year(i), False)

if __name__ == "__main__":
	unittest.main()
