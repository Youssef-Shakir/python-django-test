from city_fucnction import sorted_name
import unittest
class country_test(unittest.TestCase):
	def test_city_name(self):
		city_name = sorted_name('baghdad','iraq')
		self.assertEqual(city_name,'baghdad iraq')
	def test_city_name_pop(slef):
		city_name_pop = sorted_name('baghdad','iraq','500000')
		slef.assertEqual(city_name,'baghdad iraq 500000')


if __name__ == '__main__':
	unittest.main()
